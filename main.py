from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import importlib

load_dotenv()

static_dir = os.path.join(os.path.dirname(__file__), "frontend", "dist")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_dir = os.path.join(os.path.dirname(__file__), 'backend', 'api')

for filename in os.listdir(api_dir):
    if filename.endswith("_router.py"):
        module_name = filename[:-3]
        module = importlib.import_module(f"backend.api.{module_name}")

        if hasattr(module, 'router'):
            app.include_router(module.router)

app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
