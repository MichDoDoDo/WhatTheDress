from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, UUID
from datetime import datetime, timezone 
from core.database import Base
from uuid import UUID


class User(Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    username:Mapped[str] = mapped_column(String(20), unique= True, nullable=False)
    email: Mapped[str] = mapped_column(String (64),unique=True,nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    
    