from typing import Optional
from pydantic import BaseModel, Field, constr, create_model


class SchemaAuthor(BaseModel):
    firstname: constr(strict=True, min_length=2, max_length=50) = Field(...)
    lastname: constr(strict=True, min_length=2, max_length=50) = Field(...)

    class config:
        schema_extra = {
            "ejemplo": {
                "firstname": "John",
                "lastname": "Doe",
            }
        }


class UpdateAuthorModel(BaseModel):
    firstname: Optional[constr(strict=True, min_length=2, max_length=50)]
    lastname: Optional[constr(strict=True, min_length=2, max_length=50)]

    class config:
        schema_extra = {
            "ejemplo": {
                "firstname": "John",
                "lastname": "Doe",
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
