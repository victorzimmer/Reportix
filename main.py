from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
@app.get("/index.html", response_class=HTMLResponse)
def read_root():
    index = open("client/index.html")
    return index.read()


@app.get("/update/{field_id}")
def read_item(field_id: str):
    return {"item_id": item_id, "q": q}
