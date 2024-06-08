from typing import Union

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse
from starlette.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

DIST_SRC = "reportix-vue/dist/"
PDF_SRC = "pdf/"

availableModels = ["Phi", "Llama 2", "Llama 3"]
selectedModel = ""
availableTemplates = ["Formal", "Simple", "Fun"]
selectedTemplate = None
author = ""
documentTitle = ""
documentSubtitle = ""
documentDate = ""


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

@app.get("/pdf/{file_path:path}", response_class=FileResponse)
def read_static_file(file_path: str):
    return PDF_SRC+file_path


@app.get("/textfield/{field_id}", response_class=HTMLResponse)
def read_item(field_id: str):
    return {"item_id": field_id}


############
#  Title   #
############
@app.get("/settings/title", response_class=JSONResponse)
def get_title():
    return documentTitle

class TitleUpdate(BaseModel):
    title: str

@app.post("/settings/title", response_class=JSONResponse)
def set_title(titleUpdate: TitleUpdate):
    global documentTitle
    documentTitle = titleUpdate.title
    print("Updated title", documentTitle)
    return documentTitle



############
# Subtitle #
############
@app.get("/settings/subtitle", response_class=JSONResponse)
def get_subtitle():
    return documentSubtitle

class SubtitleUpdate(BaseModel):
    subtitle: str

@app.post("/settings/subtitle", response_class=JSONResponse)
def set_subtitle(subtitleUpdate: SubtitleUpdate):
    global documentSubtitle
    documentSubtitle = subtitleUpdate.subtitle
    print("Updated subtitle", documentSubtitle)
    return documentSubtitle


############
#  Author  #
############
@app.get("/settings/author", response_class=JSONResponse)
def get_author():
    return author

class AuthorUpdate(BaseModel):
    author: str

@app.post("/settings/author", response_class=JSONResponse)
def set_author(authorUpdate: AuthorUpdate):
    global author
    author = authorUpdate.author
    print("Updated author", author)
    return author

############
#   Date   #
############
@app.get("/settings/date", response_class=JSONResponse)
def get_date():
    return documentDate

class DateUpdate(BaseModel):
    date: str

@app.post("/settings/date", response_class=JSONResponse)
def set_date(dateUpdate: DateUpdate):
    global documentDate
    documentDate = dateUpdate.date
    print("Updated date", documentDate)
    return documentDate


############
#  Model   #
############
@app.get("/settings/available_models", response_class=JSONResponse)
def get_available_models():
    return availableModels

@app.get("/settings/selected_model", response_class=JSONResponse)
def get_selected_model():
    return selectedModel

class ModelSelection(BaseModel):
    modelName: str

@app.post("/settings/selected_model", response_class=JSONResponse)
def set_selected_model(modelSelection: ModelSelection):
    global selectedModel
    if (modelSelection.modelName in availableModels):
        selectedModel = modelSelection.modelName
        print("Updated selected model", selectedModel)
        return selectedModel
    else:
        print("Attempt to select model that is not available: ", modelSelection.modelName)
        raise HTTPException(424)

############
# Template #
############
@app.get("/settings/available_templates", response_class=JSONResponse)
def get_available_templates():
    return availableTemplates

@app.get("/settings/selected_template", response_class=JSONResponse)
def get_selected_template():
    return selectedTemplate

class TemplateSelection(BaseModel):
    templateName: str

@app.post("/settings/selected_template", response_class=JSONResponse)
def set_selected_template(templateSelection: TemplateSelection):
    global selectedTemplate
    if (templateSelection.templateName in availableTemplates):
        selectedTemplate = templateSelection.templateName
        print("Updated selected template", selectedTemplate)
        return selectedTemplate
    else:
        print("Attempt to select template that is not available: ", templateSelection.templateName)
        raise HTTPException(424)


# @app.update("/textfield/{field_id}", response_class=HTMLResponse)
# def read_item(field_id: str):
#     return {"item_id": field_id}
