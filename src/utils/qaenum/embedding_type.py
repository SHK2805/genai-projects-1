from enum import Enum

from src.constants import ollama_embeddings_model_name, openai_embeddings_model_name


# class syntax
class EmbeddingTypes(Enum):
    OPENAI = openai_embeddings_model_name
    OLLAMA = ollama_embeddings_model_name

# Accessing the value of an enum
embed_value = EmbeddingTypes.OLLAMA.value
print(embed_value)  # Output: openai_embeddings_model_name