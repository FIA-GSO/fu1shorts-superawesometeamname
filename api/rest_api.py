from typing import Union

from fastapi import FastAPI
from .crud import create_short, read_short, read_all, read_short_random, delete_short

app = FastAPI()

@app.post("/shorts/")
def create_short_api(url: str):
    return create_short(url)
 
@app.get("/shorts/{id}")
def read_short_api(id: int):
    return read_short(id)
 
@app.get("/shorts/")
def read_all_api():
    return read_all()
 
@app.get("/shorts/random")
def read_random_api():
    return read_short_random()
 
@app.delete("/shorts/{id}")
def delete_short_api(id: int):
    delete_short(id)
    return {"status": "deleted"}
 