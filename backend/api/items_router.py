import os
import json
from typing import Optional, List
from fastapi import HTTPException, APIRouter, UploadFile, File, Form
from backend.utils.db_helpers import query_all, query_one, save_file_sync, insert_into_table

router = APIRouter()
STORAGE_DIR = "storage/items"
os.makedirs(STORAGE_DIR, exist_ok=True)


@router.get("/api/worlds/{world_id}/items")
async def get_items(world_id: int):
    rows = query_all(
        "SELECT * FROM items WHERE world_id = ?",
        (world_id,)
    )
    if not rows:
        raise HTTPException(status_code=404, detail="No items found")
    return rows


@router.get("/api/worlds/{world_id}/items/{item_id}")
async def get_item(world_id: int, item_id: int):
    row = query_one(
        "SELECT * FROM items WHERE world_id = ? AND item_id = ?",
        (world_id, item_id)
    )
    if not row:
        raise HTTPException(status_code=404, detail="Item not found")
    return row


@router.post("/api/item_add")
def add_item(
    world_id: int = Form(...),
    name: str = Form(...),
    description: Optional[str] = Form(None),
    value: int = Form(...),
    weight: int = Form(...),
    type: str = Form(...),
    cover: Optional[UploadFile] = File(None),
):
    data = {
        "world_id": world_id,
        "name": name,
        "description": description,
        "value": value,
        "weight": weight,
        "type": type,
        "cover": None
    }

    if cover:
        file_path = save_file_sync(cover, STORAGE_DIR)
        data["cover"] = file_path

    insert_into_table("items", data)

    return {"message": "Item added"}