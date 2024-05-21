from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()


@app.get("/", response_class=FileResponse)
@app.get("/index.html", response_class=FileResponse)
def read_root():
    return "client/index.html"

@app.get("/static/{filename}", response_class=FileResponse)
def read_static_file(filename: str):
    return "client/"+filename




@app.get("/textfield/{field_id}", response_class=HTMLResponse)
def read_item(field_id: str):
    return {"item_id": field_id}


# @app.update("/textfield/{field_id}", response_class=HTMLResponse)
# def read_item(field_id: str):
#     return {"item_id": field_id}
