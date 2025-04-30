from fastapi import APIRouter, HTTPException
from backend.db.database import get_db_connection
import sqlite3

router = APIRouter()


@router.get("/api/worlds/{world_id}/characters")
async def get_characters_by_world(world_id: int):
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, status, photo_path, world_id
        FROM characters
        WHERE world_id = ?
    """, (world_id,))

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=404, detail="No characters found")

    return [dict(row) for row in rows]


@router.get("/api/worlds/{world_id}/characters/{character_id}")
async def get_character_by_id(world_id: int, character_id: int):
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM characters
        WHERE id = ? AND world_id = ?
    """, (character_id, world_id))

    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Character not found")

    return dict(row)
