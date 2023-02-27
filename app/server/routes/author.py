from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
import server.db as db

from server.models.author import (
    ErrorResponseModel,
    ResponseModel,
    SchemaAuthor,
    UpdateAuthorModel
)

router = APIRouter()


@router.get("")
async def get_authors():
    return await db.Author.objects.all()


@router.get("/{id}")
async def get_author_data(id: int):
    return await db.Author.objects.get(id=id)


@router.post("")
async def create_author(author: db.Author):
    await author.save()
    return author


@router.put("/{id}")
async def update_author_data(id: int, author: UpdateAuthorModel = Body(...)):
    try:
        await db.Author.objects.get(id=id)
    except:
        raise HTTPException(status_code=404, detail="Author doesn't exist.")
    await db.Author.objects.filter(id=id).update(**author.dict())
    return ResponseModel(author, "Author updated successfully.")


@router.delete("/{id}")
async def delete_author(id: int):
    try:
        await db.Author.objects.get(id=id)
    except:
        raise HTTPException(status_code=404, detail="Author doesn't exist.")
    await db.Author.objects.filter(id=id).delete()
    return ResponseModel("Author with ID: {} removed".format(id), "Author deleted successfully.")


@router.on_event("startup")
async def startup():
    if not db.database.is_connected:
        await db.database.connect()
    # create a dummy entry
    await db.Author.objects.get_or_create(
        id=1, firstName="John", lastName="Doe"
    )
    await db.Author.objects.get_or_create(
        id=2, firstName="Jane", lastName="Doe"
    )
    await db.Author.objects.get_or_create(
        id=3, firstName="John", lastName="Smith"
    )
    await db.Author.objects.get_or_create(
        id=4, firstName="Jane", lastName="Smith"
    )


@router.on_event("shutdown")
async def shutdown():
    if db.database.is_connected:
        await db.database.disconnect()
