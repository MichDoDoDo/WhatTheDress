from fastapi import APIRouter, Depends, HTTPException
from clothing.schemas.clothing_schema import ClothingCreate, ClothingRead, ClothingUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from clothing.controllers.clothing_controller import createClothes
from core.session import get_db
clothing_router = APIRouter(prefix="/clothing")


@clothing_router.post("/", response_model=ClothingRead)
async def clothing_post( clothing: ClothingCreate, db:AsyncSession=Depends(get_db)):
    return await createClothes(db, clothing)
