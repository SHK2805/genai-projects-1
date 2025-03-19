from src.utils.common_utils import get_openai_embeddings

class EmbeddingService:
    def __init__(self):
        self.embeddings = get_openai_embeddings()

    def get_embeddings(self):
        return self.embeddings
