import os
import json
from typing import Optional, List
from fastapi import HTTPException, APIRouter, UploadFile, File, Form
from backend.utils.db_helpers import query_all, query_one, save_file_sync, insert_into_table

router = APIRouter()
STORAGE_DIR = "storage/locations"
os.makedirs(STORAGE_DIR, exist_ok=True)


@router.get("/api/worlds/{world_id}/locations")
async def get_locations(world_id: int):
    rows = query_all(
        "SELECT * FROM locations WHERE world_id = ?",
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


@router.post("/api/location_add")
def add_location(
        world_id: int = Form(...),
        name: str = Form(...),
        description: str = Form(...),
        type: Optional[str] = Form(None),
        tags: Optional[str] = Form(None),
        cover: Optional[UploadFile] = File(None),
        images_json: Optional[List[UploadFile]] = File(None)
):
    data = {
        "world_id": world_id,
        "name": name,
        "description": description,
        "type": type,
        "tags": tags,
        "cover": None,
        "images_json": "[]",
    }

    if cover:
        file_path = save_file_sync(cover, STORAGE_DIR)
        data["cover"] = file_path

    if images_json:
        saved_paths = []
        for img_file in images_json:
            path = save_file_sync(img_file, STORAGE_DIR)
            saved_paths.append(path)
        data["images_json"] = json.dumps(saved_paths)

    insert_into_table("locations", data)

    return {"message": "Location added"}
