import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv


load_dotenv()
DB_URL = os.getenv("POSTGRES_URL")
engine = create_engine(DB_URL)

localSession = sessionmaker(autocommit = False, autoflush= False, bind=engine)



class Base(DeclarativeBase):
    pass

def get_db_sessiion():
    db = localSession()
     
