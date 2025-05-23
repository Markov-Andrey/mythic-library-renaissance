from fastapi import APIRouter, HTTPException
from backend.utils.db_helpers import query_all, query_one

router = APIRouter()


@router.get("/api/worlds/{world_id}/locations")
async def get_locations(world_id: int):
    rows = query_all(
        "SELECT id, name, parent_location_id FROM locations WHERE world_id = ?",
        (world_id,)
    )
    if not rows:
        raise HTTPException(status_code=404, detail="No locations found")
    return rows


@router.get("/api/worlds/{world_id}/locations/{location_id}")
async def get_location(world_id: int, location_id: int):
    row = query_one(
        "SELECT * FROM locations WHERE world_id = ? AND id = ?",
        (world_id, location_id)
    )
    if not row:
        raise HTTPException(status_code=404, detail="Location not found")
    return row
