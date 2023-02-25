# app/db.py

import databases
import ormar
import sqlalchemy

from server.config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Author(ormar.Model):
    class Meta(BaseMeta):
        tablename = "authors"

    id: int = ormar.Integer(primary_key=True)
    firstname: str = ormar.String(max_length=100)
    lastname: str = ormar.String(max_length=100)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
