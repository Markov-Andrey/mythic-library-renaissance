import os
import json
from typing import Optional, List
from fastapi import HTTPException, APIRouter, UploadFile, File, Form
from backend.utils.db_helpers import query_all, query_one, save_file_sync, insert_into_table, execute

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


@router.get("/api/worlds/{world_id}/locations_array")
async def get_locations(world_id: int):
    rows = query_all(
        "SELECT id, name FROM locations WHERE world_id = ?",
        (world_id,)
    )
    if not rows:
        raise HTTPException(status_code=404, detail="No locations found")
    return rows


@router.get("/api/worlds/{world_id}/locations/{location_id}")
async def get_location(world_id: int, location_id: int):
    location = query_one(
        "SELECT * FROM locations WHERE world_id = ? AND id = ?",
        (world_id, location_id)
    )
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    parent_location = None
    parent_id = location.get("parent_location_id")
    if parent_id:
        parent_location = query_one(
            "SELECT * FROM locations WHERE world_id = ? AND id = ?",
            (world_id, parent_id)
        )

    children = query_all(
        "SELECT * FROM locations WHERE world_id = ? AND parent_location_id = ?",
        (world_id, location_id)
    )

    location["parent"] = parent_location
    location["children"] = children or []

    return location


@router.delete("/api/worlds/{world_id}/locations/{location_id}")
async def delete_location(world_id: int, location_id: int):
    execute(
        "DELETE FROM locations WHERE world_id = ? AND id = ?",
        (world_id, location_id)
    )
    return {"detail": "Location deleted"}


@router.post("/api/location_add")
def add_location(
        world_id: int = Form(...),
        name: str = Form(...),
        description: str = Form(...),
        type: Optional[str] = Form(None),
        tags: Optional[str] = Form(None),
        parent_location_id: Optional[int] = Form(None),
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
        "parent_location_id": parent_location_id
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


@router.post("/api/location_edit")
def update_location(
    location_id: int = Form(...),
    world_id: int = Form(...),
    name: str = Form(...),
    description: str = Form(...),
    type: Optional[str] = Form(None),
    tags: Optional[str] = Form(None),
    parent_location_id: Optional[str] = Form(None),
    cover: Optional[UploadFile] = File(None),
    images_json: Optional[List[UploadFile]] = File(None),
    images_to_delete: Optional[str] = Form(None),
):
    location = query_one(
        "SELECT * FROM locations WHERE world_id = ? AND id = ?",
        (world_id, location_id)
    )
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    try:
        parent_id = int(parent_location_id) if parent_location_id not in [None, "", "null"] else None
    except ValueError:
        parent_id = None

    data = {
        "world_id": world_id,
        "name": name,
        "description": description,
        "type": type,
        "tags": tags,
        "parent_location_id": parent_id,
        "cover": location["cover"],
    }

    if cover:
        if location.get("cover"):
            try:
                os.remove(os.path.join(STORAGE_DIR, location["cover"]))
            except FileNotFoundError:
                pass
        data["cover"] = save_file_sync(cover, STORAGE_DIR)

    images = []
    try:
        images = json.loads(location["images_json"] or "[]")
    except:
        pass

    if images_to_delete:
        try:
            to_delete = json.loads(images_to_delete)
            for img in to_delete:
                try:
                    os.remove(os.path.join(STORAGE_DIR, img))
                except FileNotFoundError:
                    pass
            images = [img for img in images if img not in to_delete]
        except:
            pass

    if images_json:
        for f in images_json:
            images.append(save_file_sync(f, STORAGE_DIR))

    data["images_json"] = json.dumps(images)

    fields = ", ".join(f"{k} = ?" for k in data)
    execute(f"UPDATE locations SET {fields} WHERE id = ?", (*data.values(), location_id))

    return {"message": "Location updated"}