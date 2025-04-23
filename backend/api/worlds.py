import os
import uuid
from fastapi import APIRouter, UploadFile, File, Form
from backend.db.db import get_db_connection

router = APIRouter()
STORAGE_DIR = "storage/worlds"
os.makedirs(STORAGE_DIR, exist_ok=True)


@router.get("/api/worlds")
async def get_worlds():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, cover_image_path FROM worlds")
    rows = cursor.fetchall()
    conn.close()

    return [{"id": row[0], "name": row[1], "cover_image_path": row[2]} for row in rows]


@router.post("/api/worlds_add")
async def add_world(
    name: str = Form(...),
    short_description: str = Form(...),
    full_description: str = Form(...),
    visual_style: str = Form(...),
    genre: str = Form(...),
    tags: str = Form(...),
    cover_image_path: UploadFile = File(...)
):
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
            name, short_description, full_description, 
            visual_style, genre, tags, cover_image_path
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            name,
            short_description,
            full_description,
            visual_style,
            genre,
            tags,
            db_path
        )
    )
    conn.commit()
    conn.close()

    return {"message": "World add"}
