from fastapi import APIRouter, HTTPException
from backend.db.database import get_db_connection
import sqlite3

router = APIRouter()


@router.get("/api/worlds/{world_id}/organizations")
async def get_organizations_by_world(world_id: int):
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM organizations
        WHERE world_id = ?
    """, (world_id,))

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=404, detail="No organizations found")

    return [dict(row) for row in rows]
