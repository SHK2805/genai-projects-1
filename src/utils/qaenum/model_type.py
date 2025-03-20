from enum import Enum

from src.constants import ollama_llm_model_name, openai_llm_model_name


# class syntax
class LLMTypes(Enum):
    OPENAI = openai_llm_model_name
    OLLAMA = ollama_llm_model_name

# Accessing the value of an enum
llm_value = LLMTypes.OLLAMA.value
print(llm_value)