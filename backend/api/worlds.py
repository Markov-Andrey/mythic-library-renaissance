import os
import sqlite3
import uuid
from fastapi import APIRouter, UploadFile, File, Form
from backend.db.database import get_db_connection

router = APIRouter()
STORAGE_DIR = "storage/worlds"
os.makedirs(STORAGE_DIR, exist_ok=True)


@router.get("/api/worlds")
async def get_worlds():
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM worlds")
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


@router.get("/api/worlds/{id}")
async def get_world(id: int):
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM worlds WHERE id = ?
        """,
        (id,)
    )
    world = cursor.fetchone()
    conn.close()

    if world:
        return dict(world)


@router.post("/api/worlds_add")
async def add_world(
    name: str = Form(...),
    description: str = Form(...),
    visual_style: str = Form(...),
    tags: str = Form(...),
    cover_image_path: UploadFile = File(None)
):
    db_path = None

    if cover_image_path:
        ext = os.path.splitext(cover_image_path.filename)[1]
        filename = f"{uuid.uuid4().hex}{ext}"
        file_path = os.path.join(STORAGE_DIR, filename)

        with open(file_path, "wb") as buffer:
            content = await cover_image_path.read()
            buffer.write(content)

        db_path = f"/{file_path.replace(os.sep, '/')}"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO worlds (
            name, description, visual_style, tags, cover_image_path
        ) 
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            name,
            description,
            visual_style,
            tags,
            db_path
        )
    )
    conn.commit()
    conn.close()

    return {"message": "World added"}
