from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from backend.utils.db_helpers import query_all

router = APIRouter()

ALLOWED_TABLES = {
    "locations": "locations",
    "organizations": "organizations",
    "items": "items",
    "characters": "characters",
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


@router.get("/api/worlds/{world_id}/{entity}/types")
async def get_types(world_id: int, entity: str):
    query = f"SELECT DISTINCT type FROM {entity} WHERE world_id = ?"
    rows = query_all(query, (world_id,))
    if not rows:
        raise HTTPException(status_code=404, detail="No types found")
    return [row["type"] for row in rows]


@router.get("/api/worlds/{world_id}/{entity}/tags")
async def get_tags(world_id: int, entity: str):
    query = f"SELECT tags FROM {entity} WHERE world_id = ? AND tags IS NOT NULL"
    rows = query_all(query, (world_id,))

    if not rows:
        raise HTTPException(status_code=404, detail="No tags found")

    tags_set = set()
    for row in rows:
        tags = row["tags"].split(",")
        tags_set.update(t.strip() for t in tags if t.strip())

    return sorted(tags_set)
