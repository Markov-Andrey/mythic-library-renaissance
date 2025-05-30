import os
from typing import Optional
from fastapi import HTTPException, APIRouter, UploadFile, File, Form
from backend.utils.db_helpers import query_one, save_file_sync, insert_into_table

router = APIRouter()
STORAGE_DIR = "storage/characters"
os.makedirs(STORAGE_DIR, exist_ok=True)


@router.get("/api/worlds/{world_id}/character/{item_id}")
async def get_character(world_id: int, item_id: int):
    row = query_one(
        "SELECT * FROM characters WHERE world_id = ? AND id = ?",
        (world_id, item_id)
    )
    if not row:
        raise HTTPException(status_code=404, detail="Character not found")
    return row


@router.post("/api/character_add")
def add_character(
    world_id: int = Form(...),
    name: str = Form(...),
    description: Optional[str] = Form(None),
    type: Optional[str] = Form(None),
    tags: Optional[str] = Form(None),
    age: Optional[int] = Form(None),
    gender: Optional[str] = Form(None),
    race: Optional[str] = Form(None),
    character_class: Optional[str] = Form(None),
    status: Optional[str] = Form("true"),
    cover: Optional[UploadFile] = File(None)
):
    data = {
        "world_id": world_id,
        "name": name,
        "description": description,
        "type": type,
        "tags": tags,
        "age": age,
        "gender": gender,
        "race": race,
        "character_class": character_class,
        "status": status.lower() in ("true", "1", "yes"),
    }

    if cover:
        saved_path = save_file_sync(cover, STORAGE_DIR)
        data["cover"] = saved_path

    new_id = insert_into_table("characters", data)

    return {"message": "Character added", "id": new_id}
