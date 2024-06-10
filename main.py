from typing import Union

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse
from starlette.responses import JSONResponse
from pydantic import BaseModel

from random import randrange
import os
import sys
from backend.folder_digest import read_folder
from setInterval import setInterval
import shutil
from pathlib import Path
import ollama
from latex import build_pdf

try:
    ollama.list()
except:
    print("Ollama not found. Exiting.")
    sys.exit(1)

app = FastAPI()

DIST_SRC = "reportix-vue/dist/"
PDF_SRC = "pdf/"
CODE_SRC = "code_src/"
TEMPLATE_SRC = "latex-templates/"

availableModels = []
selectedModel = ""
availableTemplates = []
selectedTemplate = None
author = ""
documentTitle = ""
documentSubtitle = ""
documentDate = ""

textfields = {"introduction": "", "methods": "", "results": "", "discussion": "", "conclusion": ""}
textfieldsChangedSinceLastGeneration = False
codeChangedSinceLastAnalysis = False
textfield_suggestions = {"introduction": ["No suggestions yet"], "methods":["No suggestions yet"], "results": ["No suggestions yet"], "discussion": ["No suggestions yet"], "conclusion": ["No suggestions yet"]}


pdf_compile_randid = 0


Path("./"+CODE_SRC).mkdir(parents=True, exist_ok=True)

def loadAvailableModels():
    global availableModels
    availableModels = []
    ollamaModels = ollama.list()["models"]
    for model in ollamaModels:
        availableModels.append(model["name"])

def loadAvailableTemplates():
    global availableTemplates
    availableTemplates = []
    templateFiles = [f for f in Path().glob("./"+TEMPLATE_SRC+"*.tex")]
    for templateFile in templateFiles:
        availableTemplates.append(str(templateFile).split("/")[-1][0:-4])

loadAvailableModels()
loadAvailableTemplates()

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
    loadAvailableModels()
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
    loadAvailableTemplates()
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


##############
# Textfields #
##############
@app.get("/textfields/{field_name}", response_class=JSONResponse)
def get_textfield_content(field_name: str):
    if textfields[field_name]:
        return textfields[field_name]
    return ""

class TextfieldUpdate(BaseModel):
    content: str

@app.post("/textfields/{field_name}", response_class=JSONResponse)
def set_textfield_content(field_name: str, textfieldUpdate: TextfieldUpdate):
    textfields[field_name] = textfieldUpdate.content
    global textfieldsChangedSinceLastGeneration
    textfieldsChangedSinceLastGeneration = True
    return True



#########################
# Textfield suggestions #
#########################
@app.get("/textfield_suggestions/{field_name}", response_class=JSONResponse)
def get_textfield_content(field_name: str):
    if textfield_suggestions[field_name]:
        return textfield_suggestions[field_name]
    return ""




############
# Code SRC #
############
@app.get("/code_src/reset", response_class=JSONResponse)
def reset_code_src():
    with os.scandir(CODE_SRC) as entries:
        for entry in entries:
            if entry.is_dir() and not entry.is_symlink():
                shutil.rmtree(entry.path)
            else:
                os.remove(entry.path)
    return True

class FileUpload(BaseModel):
    fileName: str
    relativePath: str
    fileText: str

@app.post("/code_src/upload", response_class=JSONResponse)
def upload_file(fileUpload: FileUpload):
    # try:
    #     os.mkdir("./"+CODE_SRC+str.join("/", fileUpload.relativePath.split("/")[0:-1]))
    # except FileExistsError:
    #     pass
    Path("./"+CODE_SRC+str.join("/", fileUpload.relativePath.split("/")[0:-1])).mkdir(parents=True, exist_ok=True)

    f = open(CODE_SRC + fileUpload.relativePath, "w")
    f.write(fileUpload.relativePath)
    f.close()
    print("Recieved "+fileUpload.relativePath)

@app.get("/code_src/done", response_class=JSONResponse)
def process_code_src():
    global codeChangedSinceLastAnalysis
    codeChangedSinceLastAnalysis = True
    print("Done uploading files!")
    return True


###############
# Compile PDF #
###############
@app.get("/report/compile_randid", response_class=JSONResponse)
def get_last_randid_pdf():
    print("Returning PDF RandID: ", pdf_compile_randid)
    return pdf_compile_randid

@app.get("/report/compile", response_class=JSONResponse)
def compile_pdf():
    if selectedTemplate:
        latexFile = open(TEMPLATE_SRC + selectedTemplate + ".tex", "r")
        latexString = latexFile.read()
        latexFile.close()


        if documentTitle:
            latexString = latexString.replace("$Reportix:Title$", documentTitle)
        else:
            latexString = latexString.replace("$Reportix:Title$", "Title")

        if documentSubtitle:
            latexString = latexString.replace("$Reportix:Subtitle$", documentSubtitle)
        else:
            latexString = latexString.replace("$Reportix:Subtitle$", "Subtitle")

        if author:
            latexString = latexString.replace("$Reportix:Author$", author)
        else:
            latexString = latexString.replace("$Reportix:Author$", "Author")

        if documentDate:
            latexString = latexString.replace("$Reportix:Date$", documentDate)
        else:
            latexString = latexString.replace("$Reportix:Date$", "Date")

        for sectionName in textfields:
            if textfields[sectionName]:
                latexString = latexString.replace("$Reportix:Textfield-"+sectionName+"$", textfields[sectionName])
            else:
                latexString = latexString.replace("$Reportix:Textfield-"+sectionName+"$", "Content text")


        pdfBytes = build_pdf(latexString)

        # print(bytes(pdfBytes)[:10])

        pdfFile = open(PDF_SRC + "report.pdf", "wb")
        pdfFile.write(bytes(pdfBytes))
        pdfFile.close()

        global pdf_compile_randid
        pdf_compile_randid = randrange(100000000)
        print("New PDF RandID: ", pdf_compile_randid)

        return True
    return False



#################
# AI Generation #
#################
# from backend.folder_digest import model_read_files
# from backend.folder_digest import read_folder, find_paths, model_read_files
# from backend.model_response import model_response
# from backend.preprompts import project_system_template
# from backend.text_helper import reportix_model
from backend.preprompts import code_system_template, file_id_template

AI_currentSummary = "No summary generated yet."

def runAICodeAnalysis():
    print("Analyzing code!")
    global codeChangedSinceLastAnalysis
    codeChangedSinceLastAnalysis = False

    # fileListIter = os.walk(CODE_SRC)
    # fileList = []
    # for filePathObj in fileListIter:
    #     for fileName in filePathObj[2]:
    #         fileList.append(filePathObj[0] + fileName)

    # fileList = fileList[0:15]

    # # prompt = file_id_template+read_folder(CODE_SRC)
    # prompt = "\n".join(fileList)
    # print("Prompt: ", prompt)
    # modelOutput = ollama.generate(model=selectedModel, system=file_id_template, prompt=prompt)
    # print("Output: ", modelOutput["response"])

    # filesToInspect = modelOutput["response"].split("\n")[1:-1]
    # print("Files to inspect: ",filesToInspect)

    # for filePath in filesToInspect:
    #     try:
    #         fileHandle = open(CODE_SRC+filePath, "r")
    #         fileSummaryOutput = ollama.generate(model=selectedModel, prompt=code_system_template+fileHandle.read())
    #         print(fileSummaryOutput["response"])
    #     except:
    #         print("File not found, skipping file.", CODE_SRC+filePath)



    # project_structure = read_folder("../code_src/")
    # project_compressed = model_response(project_structure, project_system_template)
    # paths_to_files = find_paths(project_compressed)
    # summary = model_read_files(paths_to_files, project_structure)[1]
    # global AI_currentSummary
    # AI_currentSummary = summary

def runAIGeneration():
    global textfieldsChangedSinceLastGeneration
    textfieldsChangedSinceLastGeneration = False
    # for sectionName in textfields:
    #     return_string = reportix_model(section=sectionName, previous_suggestion=str(textfield_suggestions[sectionName]), project_summary=AI_currentSummary, text=textfields[sectionName])
    #     print("AI wrote: ", return_string)
    #     result_list = return_string.split("*")
    #     textfield_suggestions[sectionName] = result_list

    for sectionName in textfields:
        preprompt = "The user is writing an IMRaD report. This is their section about "+sectionName+" You should give the user suggestions on improvements for their text. One suggestion per line."
        prompt = textfields[sectionName]
        if prompt == "":
            prompt = "The user hasn't written anything yet. Give them some motivation?"
        modelOutput = ollama.generate(model=selectedModel, system=preprompt, prompt=prompt)
        print(sectionName, modelOutput["response"])
        suggestionListRaw = modelOutput["response"].split("\n")
        suggestionListFiltered = []
        for suggestion in suggestionListRaw:
            if len(suggestion) > 1:
                suggestionListFiltered.append(suggestion)

        textfield_suggestions[sectionName] = suggestionListFiltered

def pollAIShouldGenerate():
    print("Polling AI")
    print("Code changed:", codeChangedSinceLastAnalysis)
    print("Selected model: ", selectedModel)
    if codeChangedSinceLastAnalysis and selectedModel:
        runAICodeAnalysis()
    if textfieldsChangedSinceLastGeneration and selectedModel:
        runAIGeneration()


setInterval(5, pollAIShouldGenerate)


# @app.update("/textfield/{field_id}", response_class=HTMLResponse)
# def read_item(field_id: str):
#     return {"item_id": field_id}
