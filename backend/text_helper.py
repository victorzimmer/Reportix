
from preprompts import *
from model_response import *
from folder_digest import *



def reportix_model( text: str, 
                    previous_suggestion: str, 
                    project_summary: str,
                    system_template=correction_system_template,
                    section=str
                    ) -> str:
    """
    Live Correction of Report text

    Parameters:
    text: str
        The text to be corrected

    previous_suggestion: str
        The previous suggestion to be corrected

    project_summary: str
        The project summary for understanding of the project

    system_template: str
        The system template for the model
    
    section: str
        The section of the report where the text is located

    Returns:
    str: The corrected text
    """

    model_input = f" {section} {text} {previous_suggestion} {project_summary}"
    response = model_response(model_input, system_template)
    
    return response["message"]["content"]




if __name__ == "__main__":
    project_directory = "example_project/"

    project_structure = read_folder(project_directory)
    model_resp_mdl_strc = model_response(project_structure, project_system_template)
    print(model_resp_mdl_strc['message']['content'])
    paths = model_read_files(model_resp_mdl_strc['message']['content'])
    
    print(paths[0])
    print("\n")
    print(paths[1])

    text = "The quick brown fox jumps over the lazy dog"
    previous_suggestion = ""
    project_summary = paths[1]

    test = reportix_model(text, previous_suggestion, project_summary, correction_system_template, section="introduction")
    
    print(test)

