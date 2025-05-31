from sqlalchemy.orm import mapped_column

from pydantic import BaseModel
from uuid import UUID


class User(BaseModel):
    id:UUID
    username:str
    