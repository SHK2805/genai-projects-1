# Assuming OllamaLLM and OllamaEmbeddings are defined similarly to OpenAI models
from langchain_ollama import OllamaLLM, OllamaEmbeddings

from src.readers.platforms.base_platform import BaseLLM, BaseEmbedding


class OllamaModel(BaseLLM):
    def get_model(self, model_name):
        return OllamaLLM(model=model_name)

class OllamaEmbedding(BaseEmbedding):
    def get_embeddings(self, model_name):
        return OllamaEmbeddings(model=model_name)
