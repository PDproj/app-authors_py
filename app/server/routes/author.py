from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_author,
    delete_author,
    retrieve_author,
    retrieve_authors,
    update_author,
)

from server.models.author import (
    ErrorResponseModel,
    ResponseModel,
    SchemaAuthor,
    UpdateAuthorModel
)

router = APIRouter()


@router.get("", response_description="Authors retrieved")
async def get_authors():
    authors = await retrieve_authors()
    if authors:
        return ResponseModel(authors, "Authors data retrieved successfully")
    return ResponseModel(authors, "Empty list returned")


@router.get("/{id}", response_description="Author data retrieved")
async def get_author_data(id):
    author = await retrieve_author(id)
    if author:
        return ResponseModel(author, "Author data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Author doesn't exist.")


@router.post("", response_description="Author data added into the database")
async def add_author_data(author: SchemaAuthor = Body(...)):
    author = jsonable_encoder(author)
    new_author = await add_author(author)
    return ResponseModel(new_author, "Author added successfully.")


@router.put("/{id}")
async def update_author_data(id: str, req: UpdateAuthorModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_author = await update_author(id, req)
    if updated_author:
        return ResponseModel(
            "Author with ID: {} name update is successful".format(id),
            "Author name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the author data.",
    )


@router.delete("/{id}", response_description="Author data deleted from the database")
async def delete_author_data(id: str):
    deleted_author = await delete_author(id)
    if deleted_author:
        return ResponseModel(
            "Author with ID: {} removed".format(
                id), "Author deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Author with id {0} doesn't exist".format(id)
    )
