from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List


class ClothingBase (BaseModel):
    category: List[str]
    suitabily: List[str]
    material: List[str]
    
class ClothingCreate(ClothingBase):
    pass

class ClothingUpdate(BaseModel):
    category: Optional [List[str]]
    suitabily: Optional [List[str]]
    material: Optional [List[str]]
    
    
class ClothingRead(ClothingBase):
    id: int