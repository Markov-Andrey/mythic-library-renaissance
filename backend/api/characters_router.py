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
