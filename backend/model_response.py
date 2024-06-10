import ollama
from preprompts import *


def model_response(project_input:str, system_template:str) -> str:
    # Model response 
    model_response = ollama.chat(model='llama3', messages=[
    {"role": "system", "content": system_template},
    {"role": "user", "content": project_input},
    ])
    return model_response