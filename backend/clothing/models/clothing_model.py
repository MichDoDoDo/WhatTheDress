from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, Integer, String
from datetime import datetime, timezone 
from core.database import base
from sqlalchemy.dialects.postgresql import ARRAY


class Clothing(base):
    __tablename__ = "clothing"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category:Mapped[list[str]] = mapped_column(ARRAY(String),nullable=False)
    material: Mapped[list[str]] = mapped_column(ARRAY(String),nullable=False)
    suitability :Mapped[list] = mapped_column(ARRAY(String), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    
    

    