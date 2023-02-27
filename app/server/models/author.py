from typing import Optional
from pydantic import BaseModel, Field, constr


class SchemaAuthor(BaseModel):
    firstName: constr(strict=True, min_length=2, max_length=50) = Field(...)
    lastName: constr(strict=True, min_length=2, max_length=50) = Field(...)

    class config:
        schema_extra = {
            "ejemplo": {
                "firstName": "John",
                "lastName": "Doe",
            }
        }


class UpdateAuthorModel(BaseModel):
    firstname: Optional[constr(strict=True, min_length=2, max_length=50)]
    lastname: Optional[constr(strict=True, min_length=2, max_length=50)]

    class config:
        schema_extra = {
            "ejemplo": {
                "firstName": "John",
                "lastName": "Doe",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
