import os
import sqlite3
import json
from typing import Optional, List
from backend.db.database import get_db_connection
from fastapi import HTTPException, APIRouter, UploadFile, File, Form
from backend.utils.db_helpers import query_all, query_one, save_file_sync, insert_into_table

router = APIRouter()
STORAGE_DIR = "storage/characters"
os.makedirs(STORAGE_DIR, exist_ok=True)


@router.post("/api/character_add")
def add_character(
    world_id: int = Form(...),
    name: str = Form(...),
    description: Optional[str] = Form(None),
    type: Optional[str] = Form(None),
    age: Optional[int] = Form(None),
    gender: Optional[str] = Form(None),
    race: Optional[str] = Form(None),
    character_class: Optional[str] = Form(None),
    status: Optional[bool] = Form(True),
    photo_path: Optional[UploadFile] = File(None)
):
    data = {
        "world_id": world_id,
        "name": name,
        "description": description,
        "type": type,
        "age": age,
        "gender": gender,
        "race": race,
        "character_class": character_class,
        "status": status,
        "photo_path": None
    }

    if photo_path:
        saved_path = save_file_sync(photo_path, STORAGE_DIR)
        data["photo_path"] = saved_path

    insert_into_table("characters", data)

    return {"message": "Character added"}
