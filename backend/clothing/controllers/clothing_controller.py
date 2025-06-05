from sqlalchemy.ext.asyncio import AsyncSession
from clothing.models.clothing_model import Clothing
from clothing.schemas.clothing_schema import ClothingSchema

async def createClothes(db: AsyncSession, item: ClothingSchema ):
    add_item = Clothing(
        category = item.category,
        materials = item.material,
        suitability = item.suitabily
    )
    
    db.add(add_item)
    await db.commit()
    await db.refresh(add_item)
    return add_item
    
    