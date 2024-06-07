import ollama
from preprompts import *


def model_response(user_input:str, system_template:str) -> str:
    # Model response 
    model_response = ollama.chat(model='llama3', messages=[
    {"role": "system", "content": system_template},
    {"role": "user", "content": user_input},
    ])
    return model_response



if __name__ == "__main__":
    # Example usage
    user_input_code = """
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    print(add(5, 3))
    print(subtract(5, 3))
    """
    print(model_response(user_input_code, code_system_template)['message']['content'])