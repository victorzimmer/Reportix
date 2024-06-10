
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