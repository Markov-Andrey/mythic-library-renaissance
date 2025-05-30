import os
from typing import Optional
from fastapi import HTTPException, APIRouter, UploadFile, File, Form
from backend.utils.db_helpers import query_one, save_file_sync, insert_into_table

router = APIRouter()
STORAGE_DIR = "storage/abilities"
os.makedirs(STORAGE_DIR, exist_ok=True)


@router.get("/api/worlds/{world_id}/abilities/{item_id}")
async def get_item(world_id: int, item_id: int):
    row = query_one(
        "SELECT * FROM abilities WHERE world_id = ? AND id = ?",
        (world_id, item_id)
    )
    if not row:
        raise HTTPException(status_code=404, detail="Item not found")
    return row


@router.post("/api/abilitie_add")
def add_item(
    world_id: int = Form(...),
    name: str = Form(...),
    description: Optional[str] = Form(None),
    type: str = Form(...),
    tags: str = Form(...),
    cover: Optional[UploadFile] = File(None),
):
    data = {
        "world_id": world_id,
        "name": name,
        "description": description,
        "type": type,
        "tags": tags,
        "cover": None
    }

    if cover:
        file_path = save_file_sync(cover, STORAGE_DIR)
        data["cover"] = file_path

    insert_into_table("abilities", data)

    return {"message": "Abilitie added"}