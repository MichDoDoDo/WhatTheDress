from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List


class Clothing (BaseModel):
    id:Optional[UUID] = None
    category: str
    color: str
    suitabily: List[str]
