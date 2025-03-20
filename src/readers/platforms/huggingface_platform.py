from langchain_huggingface import HuggingFaceEmbeddings

from src.constants import hf_embeddings_model_name
from src.readers.platforms.base_platform import BaseLLM, BaseEmbedding


class HuggingfaceModel(BaseLLM):
    def get_model(self, model_name):
        # return HuggingFaceEmbeddings(model=model_name)
        # raise ValueError("No model defined for Huggingface")
        return None

class HuggingfaceEmbedding(BaseEmbedding):
    def get_embeddings(self, model_name):
        model_name = hf_embeddings_model_name
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': False}
        hf = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
        return hf
