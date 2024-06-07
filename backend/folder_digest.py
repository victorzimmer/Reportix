import os
from model_response import *

# need to feed this with the uploaded project from UI
def read_folder(directory:str) -> str:
    """
    Traverse project folder and pick important files.
    Compressing the project into fewer files
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


def model_read_files(project_directory:str) -> str:
    """
    Read each file which the llama3 deem important through read_folder function
    """
    stack = []
    paths = []
    for char in project_directory:
        if "[" in stack and char != "]":
            paths.append(char)

        if char == "[":
            stack.append(char)
        if char == "]":
            break
    out = "".join(paths)
    return out
    


if __name__ == "__main__":
    project_directory = "example_project/"
    project_structure = read_folder(project_directory)
    model_response = model_response(project_structure, project_system_template)
    paths = model_read_files(model_response['message']['content'])
    print(model_response['message']['content'])
    print("\n")
    print("(" + paths.split(",") + ")")
