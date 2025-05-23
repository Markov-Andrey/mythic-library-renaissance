import os
import json
from fastapi import HTTPException, APIRouter, UploadFile, File, Form
from backend.utils.db_helpers import query_all, query_one, save_file_sync, insert_into_table
from typing import Optional, List

router = APIRouter()
STORAGE_DIR = "storage/organizations"
os.makedirs(STORAGE_DIR, exist_ok=True)


@router.get("/api/worlds/{world_id}/organizations")
async def get_locations(world_id: int):
    rows = query_all(
        "SELECT * FROM organizations WHERE world_id = ?",
        (world_id,)
    )
    if not rows:
        raise HTTPException(status_code=404, detail="No organizations found")
    return rows


@router.get("/api/worlds/{world_id}/organizations/{organisation_id}")
async def get_location(world_id: int, organisation_id: int):
    row = query_one(
        "SELECT * FROM organizations WHERE world_id = ? AND id = ?",
        (world_id, organisation_id)
    )
    if not row:
        raise HTTPException(status_code=404, detail="Location not found")
    return row


@router.post("/api/organization_add")
def add_organization(
        world_id: int = Form(...),
        name: str = Form(...),
        description: str = Form(...),
        tags: Optional[str] = Form(None),
        status: bool = Form(True),
        cover: Optional[UploadFile] = File(None),
        images_json: Optional[List[UploadFile]] = File(None)
):
    data = {
        "world_id": world_id,
        "name": name,
        "description": description,
        "tags": tags,
        "status": status,
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

    insert_into_table("organizations", data)

    return {"message": "Organization added"}
