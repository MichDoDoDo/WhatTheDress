from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, UUID
from datetime import datetime, timezone 
from core.database import Base
from uuid import UUID


class Clothing(Base):
    __tablename__ = "clothing"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    category:Mapped[list] = mapped_column(list,nullable=False)
    material: Mapped[str] = mapped_column(list,nullable=False)
    suitability :Mapped[list] = mapped_column(list, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    
    

    