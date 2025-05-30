import os
import json
from typing import Optional, List
from fastapi import HTTPException, APIRouter, UploadFile, File, Query, Request
from backend.utils.db_helpers import query_all, save_file_sync, insert_into_table, execute

router = APIRouter()

ALLOWED_TABLES = {
    "locations": "locations",
    "organizations": "organizations",
    "items": "items",
    "characters": "characters",
    "abilities": "abilities",
}


@router.get("/api/worlds/{world_id}/{entity}")
async def get_entities(
        world_id: int,
        entity: str,
        type: Optional[str] = Query(default=None),
        tags: Optional[List[str]] = Query(default=None),
        search: Optional[str] = Query(default=None),
):
    if entity not in ALLOWED_TABLES:
        raise HTTPException(status_code=400, detail="Invalid entity type")

    table = ALLOWED_TABLES[entity]

    base_query = f"SELECT * FROM {table} WHERE world_id = ?"
    params = [world_id]

    if type:
        base_query += " AND type = ?"
        params.append(type)

    if tags:
        for tag in tags:
            base_query += " AND tags LIKE ?"
            params.append(f"%{tag}%")

    if search:
        base_query += " AND name LIKE ?"
        params.append(f"%{search}%")

    return query_all(base_query, tuple(params))


@router.post("/api/{entity}/add")
async def add_entity(
    entity: str,
    request: Request,
    cover: Optional[UploadFile] = File(None),
    images_json: Optional[List[UploadFile]] = File(None)
):
    if entity not in ALLOWED_TABLES:
        raise HTTPException(status_code=400, detail="Invalid entity")

    STORAGE_DIR = f"storage/{entity}"
    os.makedirs(STORAGE_DIR, exist_ok=True)

    form = await request.form()
    data = {}

    for key, value in form.items():
        if value == "" or value.lower() == "null":
            data[key] = None
        elif value.isdigit():
            data[key] = int(value)
        else:
            try:
                data[key] = float(value)
            except ValueError:
                if value.lower() in ("true", "false"):
                    data[key] = value.lower() == "true"
                else:
                    data[key] = value

    if cover:
        data["cover"] = save_file_sync(cover, STORAGE_DIR)

    if images_json:
        saved_paths = [save_file_sync(f, STORAGE_DIR) for f in images_json]
        data["images_json"] = json.dumps(saved_paths)

    if entity == "locations" and "parent_location_id" in data:
        try:
            data["parent_location_id"] = int(data["parent_location_id"])
        except (ValueError, TypeError):
            data["parent_location_id"] = None

    table = ALLOWED_TABLES[entity]
    inserted_id = insert_into_table(table, data)

    return {"message": f"{entity.capitalize()} added", "id": inserted_id}


@router.get("/api/worlds/{world_id}/{entity}/meta/types")
async def get_types(world_id: int, entity: str):
    query = f"SELECT DISTINCT type FROM {entity} WHERE world_id = ?"
    rows = query_all(query, (world_id,))
    return [row["type"] for row in rows if row["type"]]


@router.get("/api/worlds/{world_id}/{entity}/meta/tags")
async def get_tags(world_id: int, entity: str):
    query = f"SELECT tags FROM {entity} WHERE world_id = ? AND tags IS NOT NULL"
    rows = query_all(query, (world_id,))
    tags_set = set()
    for row in rows:
        tags = row["tags"].split(",")
        tags_set.update(t.strip() for t in tags if t.strip())

    return sorted(tags_set)


@router.delete("/api/worlds/{world_id}/{entity}/{item_id}")
async def delete_entity(world_id: int, entity: str, item_id: int):
    if entity not in ALLOWED_TABLES:
        raise HTTPException(status_code=400, detail="Invalid entity")

    table = ALLOWED_TABLES[entity]
    query = f"DELETE FROM {table} WHERE world_id = ? AND id = ?"
    execute(query, (world_id, item_id))
    return {"detail": f"{entity.capitalize()} deleted"}