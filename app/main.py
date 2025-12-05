from fastapi import FastAPI
from typing import Union
import json
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 解决跨域问题
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str,None] = None):
#     return {"item_id": item_id, "q": q}

def load_data():
  with open(Path(__file__).parent / "data.json",encoding="utf-8") as f:
    return json.load(f)

@app.get("/local_data")
async def local_data():
  return load_data()