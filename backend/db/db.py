from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./mythic_library.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), "mythic_library.db")
    return sqlite3.connect(db_path)


def create_database():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
