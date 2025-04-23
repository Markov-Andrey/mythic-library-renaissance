from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from backend.db.db import get_db_connection


class World(BaseModel):
    id: int
    name: str
    cover_image_path: str


router = APIRouter()


@router.get("/api/worlds", response_model=List[World])
async def get_worlds():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, cover_image_path FROM worlds")
    rows = cursor.fetchall()
    conn.close()
    return [World(id=row[0], name=row[1], cover_image_path=row[2]) for row in rows]
