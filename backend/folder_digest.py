import os
import ollama
# from model_response import *
import tiktoken
from tiktoken.load import load_tiktoken_bpe
from backend.preprompts import code_system_template, file_id_template, project_system_template


def model_response(project_input:str, system_template:str) -> str:
    # Model response
    model_response = ollama.chat(model='llama3', messages=[
    {"role": "system", "content": system_template},
    {"role": "user", "content": project_input},
    ])
    return model_response



# need to feed this with the uploaded project from UI
def read_folder(directory:str) -> str:
    """
    Traverse project folder and return the structure of the project folder
    """
    folder_structure = []

    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * level
        folder_structure.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            folder_structure.append(f"{subindent}{file}")

    return "\n".join(folder_structure)


def find_paths(directory:str) -> list[str]:
    """

    """

    stack = []
    paths = []
    for char in directory:
        if "[" in stack and char != "]":
            paths.append(char)

        if char == "[":
            stack.append(char)
        if char == "]":
            break

    out = "".join(paths)
    elements = out.strip("[]").split(',')

    return [element.strip() for element in elements]


def model_read_files(path_list:list[str], original_project_structure:str, project_directory:str) -> str:
    fileListIter = os.walk(project_directory)
    fileList = []
    for filePathObj in fileListIter:
        for fileName in filePathObj[2]:
            fileList.append(filePathObj[0] + "/" + fileName)

    # for filePath in fileList:
    #     print(filePath)

    # chunking the files and reading these in chunks
    chunk_size = 0
    chunk = ""
    max_context = 8192
    tokenizer = tiktoken.get_encoding("cl100k_base")
    chunk_responses = []
    project_directory = project_directory

    if path_list == ['']:
        # model resp
        while path_list == ['']:
            model_response_paths = model_response(original_project_structure, project_system_template)
            path_list = find_paths(model_response_paths["message"]["content"])

    for idx, path in enumerate(path_list):
        path = path.replace("//", "/")
        path = path.replace("/app/", "/")

        for filePath in fileList:
            if path in filePath:
                print(f"Replacing path {path} with {filePath}")
                path = filePath

        print(f"Index: {idx}")
        try:
            with open(path, "r") as file:
                content = project_directory + path+ ": " + file.read()
                encoded = tokenizer.encode(content)
                chunk_size += len(encoded)

                # if chunk overflow context window
                if chunk_size > max_context:
                    chunk_size -= len(encoded)

                    chunk_digest = model_response(chunk, code_system_template)
                    chunk_responses.append(chunk_digest["message"]["content"])

                    # reset chunk
                    chunk_size = 0
                    chunk = ""

                else:
                    chunk += content

                # no more files to read and chunk not full
                if idx == len(path_list) - 1:
                    chunk_digest = model_response(chunk, code_system_template)
                    chunk_responses.append(chunk_digest["message"]["content"])
        except:
            pass
            # print(f"Skipping non-existent file: {path}")

    return path_list, chunk_responses

if __name__ == "__main__":
    read_folder = read_folder("../client/")
    model_folder = model_response(read_folder, project_system_template)
    path_list = find_paths(model_folder)
    print(path_list)
    model_read_files = model_read_files(path_list, read_folder, "../client/")
    print(model_read_files[1])
