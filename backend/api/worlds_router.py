import os
from fastapi import HTTPException, APIRouter, UploadFile, File, Form
from backend.utils.db_helpers import query_all, query_one, save_file_sync, insert_into_table

router = APIRouter()
STORAGE_DIR = "storage/worlds"
os.makedirs(STORAGE_DIR, exist_ok=True)


@router.get("/api/worlds")
def get_worlds():
    return query_all("SELECT * FROM worlds")


@router.get("/api/worlds/{id}")
def get_world(id: int):
    world = query_one("SELECT * FROM worlds WHERE id = ?", (id,))
    if not world:
        raise HTTPException(status_code=404, detail="World not found")
    return world


@router.post("/api/worlds_add")
def add_world(
        name: str = Form(...),
        description: str = Form(...),
        visual_style: str = Form(...),
        tags: str = Form(...),
        cover: UploadFile = File(None)
):
    data = {
        "name": name,
        "description": description,
        "visual_style": visual_style,
        "tags": tags,
        "cover": None
    }

    if cover:
        file_path = save_file_sync(cover, STORAGE_DIR)
        data["cover"] = f"{file_path}"

    insert_into_table("worlds", data)
    return {"message": "World added"}
