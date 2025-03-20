from langchain.llms import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings

from src.readers.platforms.base_platform import BaseLLM, BaseEmbedding


class OpenAIModel(BaseLLM):
    def get_model(self, model_name):
        return ChatOpenAI(model=model_name)

class OpenAIEmbedding(BaseEmbedding):
    def get_embeddings(self, model_name):
        return OpenAIEmbeddings(model=model_name)
