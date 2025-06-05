from fastapi import APIRouter, Depends, HTTPException
from clothing.schemas.clothing_schema import ClothingCreate
from sqlalchemy.ext.asyncio import AsyncSession
from clothing.controllers.clothing_controller import createClothes
from core.database import getDBSession
clothing_router = APIRouter(prefix="/clothing")


@clothing_router.post("/", response_model=ClothingCreate)
def clothing_post( clothing = ClothingSchema, db:AsyncSession=Depends(getDBSession)):
    return createClothes(db, clothing)
