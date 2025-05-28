import os
import json
from typing import Optional, List
from fastapi import HTTPException, APIRouter, UploadFile, File, Form, Query
from backend.utils.db_helpers import query_all, query_one, save_file_sync, insert_into_table, execute

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


@router.post("/api/organization_edit")
def update_organization(
    organization_id: int = Form(...),
    world_id: int = Form(...),
    name: str = Form(...),
    description: str = Form(...),
    type: Optional[str] = Form(None),
    tags: Optional[str] = Form(None),
    cover: Optional[UploadFile] = File(None),
    images_json: Optional[List[UploadFile]] = File(None),
    images_to_delete: Optional[str] = Form(None),
):
    location = query_one(
        "SELECT * FROM organizations WHERE world_id = ? AND id = ?",
        (world_id, organization_id)
    )
    if not location:
        raise HTTPException(status_code=404, detail="Organization not found")

    data = {
        "world_id": world_id,
        "name": name,
        "description": description,
        "type": type,
        "tags": tags,
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
    execute(f"UPDATE organizations SET {fields} WHERE id = ?", (*data.values(), organization_id))

    return {"message": "Location updated"}