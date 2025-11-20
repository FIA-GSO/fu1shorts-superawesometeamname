from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .crud import create_short, read_short, read_all, read_short_random, delete_short

app = FastAPI()


# Model Pydantic to create a short
class ShortCreate(BaseModel):
    url: str


@app.post("/shorts")
def api_create_short(short: ShortCreate):
    new_id = create_short(short.url)
    return {"id": new_id, "url": short.url}


@app.get("/shorts/{short_id}")
def api_read_short(short_id: int):
    try:
        url = read_short(short_id)
        return {"id": short_id, "url": url}
    except:
        raise HTTPException(status_code=404, detail="Short not found")


@app.get("/shorts")
def api_read_all_shorts():
    shorts = read_all()
    return {"shorts": shorts}


@app.get("/shorts/random")
def api_read_random_short():
    url = read_short_random()
    return {"url": url}


@app.delete("/shorts/{short_id}")
def api_delete_short(short_id: int):
    delete_short(short_id)
    return {"status": "deleted", "id": short_id}
