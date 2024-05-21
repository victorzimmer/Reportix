from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

DIST_SRC = "reportix-vue/dist/"



@app.get("/", response_class=FileResponse)
@app.get("/index.html", response_class=FileResponse)
def read_root():
    return DIST_SRC+"index.html"

@app.get("/static/{file_path:path}", response_class=FileResponse)
def read_static_file(file_path: str):
    return DIST_SRC+file_path


@app.get("/static/{file_path:path}", response_class=FileResponse)
def read_static_file(file_path: str):
    return DIST_SRC+file_path

@app.get("/textfield/{field_id}", response_class=HTMLResponse)
def read_item(field_id: str):
    return {"item_id": field_id}


# @app.update("/textfield/{field_id}", response_class=HTMLResponse)
# def read_item(field_id: str):
#     return {"item_id": field_id}
