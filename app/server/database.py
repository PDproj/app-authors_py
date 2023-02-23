import os
import motor.motor_asyncio
from bson.objectid import ObjectId


client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])

database = client.distribuida

authors_collection = database.get_collection("authors_collections")


def author_helper(author) -> dict:
    return {
        "id": str(author["_id"]),
        "first_name": author["firstname"],
        "last_name": author["lastname"],
    }

# Retrieve all authors present in the database


async def retrieve_authors():
    authors = []
    async for author in authors_collection.find():
        authors.append(author_helper(author))
    return authors

# Add a new author into to the database


async def add_author(author_data: dict) -> dict:
    author = await authors_collection.insert_one(author_data)
    new_author = await authors_collection.find_one({"_id": author.inserted_id})
    return author_helper(new_author)

# Retrieve a author with a matching ID


async def retrieve_author(id: str) -> dict:
    author = await authors_collection.find_one({"_id": ObjectId(id)})
    if author:
        return author_helper(author)

# Update a author with a matching ID


async def update_author(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    author = await authors_collection.find_one({"_id": ObjectId(id)})
    if author:
        updated_author = await authors_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_author:
            return True
        return False

# Delete a author from the database


async def delete_author(id: str):
    author = await authors_collection.find_one({"_id": ObjectId(id)})
    if author:
        await authors_collection.delete_one({"_id": ObjectId(id)})
        return True
