import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv


load_dotenv()
DB_URL = os.getenv("POSTGRES_URL")
engine = create_async_engine(DB_URL, ehco = True)

AsyncSessionLocal = async_sessionmaker(bind = engine, autoflush=False, autocommit = False)

async def getDBSession():
    async with AsyncSessionLocal() as session:
        yield session

class Base(DeclarativeBase):
    pass




