from fastapi import APIRouter, HTTPException
from backend.db.database import get_db_connection
import sqlite3

router = APIRouter()


@router.get("/api/worlds/{world_id}/locations")
async def get_locations(world_id: int):
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, parent_location_id FROM locations WHERE world_id = ?", (world_id,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=404, detail="No locations found")

    return [{"id": row["id"], "name": row["name"], "parent_location_id": row["parent_location_id"]} for row in rows]


@router.get("/api/worlds/{world_id}/locations/{location_id}")
async def get_location(world_id: int, location_id: int):
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM locations WHERE world_id = ? AND id = ?", (world_id, location_id))
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Location not found")

    return dict(row)
