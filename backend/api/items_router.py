from fastapi import APIRouter, HTTPException
from backend.db.database import get_db_connection
import sqlite3

router = APIRouter()


@router.get("/api/worlds/{world_id}/items")
async def get_items_by_world(world_id: int):
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, description, value, weight, type
        FROM items
        WHERE world_id = ?
    """, (world_id,))

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=404, detail="No items found")

    return [dict(row) for row in rows]


@router.get("/api/worlds/{world_id}/items/{item_id}")
async def get_item_by_id(world_id: int, item_id: int):
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM items
        WHERE id = ? AND world_id = ?
    """, (item_id, world_id))

    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Item not found")

    return dict(row)
