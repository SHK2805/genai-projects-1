from src.utils.common_utils import get_openai_embeddings, get_ollama_embeddings
from src.utils.qaenum.embedding_type import EmbeddingTypes


class EmbeddingService:
    def __init__(self, embeddings_type: EmbeddingTypes = EmbeddingTypes.OPENAI):
        self.embeddings_type = embeddings_type

    def get_embeddings_type(self):
        return self.embeddings_type

    def get_default_embeddings_model_name(self):
        """Fetches the default embeddings model name based on the selected embeddings type."""
        if self.embeddings_type not in EmbeddingTypes:
            raise ValueError("Invalid embeddings type.")
        return self.embeddings_type.value  # Directly access enum value

    def get_embeddings_model(self, model_name: str = None, model_type: EmbeddingTypes = None):
        """Fetches the embedding model based on the type and model name."""
        model_type = model_type or self.embeddings_type
        model_name = model_name or model_type.value

        # Ensure model_name is a string, not a tuple
        if isinstance(model_name, tuple):
            model_name = model_name[0]  # Extract the first element if it's a tuple

        print(f"Getting embeddings model: {model_name} of type: {model_type}")

        # Use a dictionary to map model types to corresponding functions
        embedding_function_map = {
            EmbeddingTypes.OPENAI: get_openai_embeddings,
            EmbeddingTypes.OLLAMA: get_ollama_embeddings,
        }

        embedding_function = embedding_function_map.get(model_type)

        if not embedding_function:
            raise ValueError("Invalid embeddings type.")

        return embedding_function(model_name)
