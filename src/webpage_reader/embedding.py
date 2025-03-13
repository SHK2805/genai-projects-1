from langchain_openai import OpenAIEmbeddings


class DataEmbedder:
    def __init__(self, model_name=None):
        self.model_name = model_name
        if model_name is None:
            self.embedder = OpenAIEmbeddings()
        else:
            self.embedder = OpenAIEmbeddings(model=model_name)

    def embed(self, text):
        return self.embedder.embed(text)

    def embed_batch(self, texts):
        return self.embedder.embed_batch(texts)

    def get_model_name(self):
        return self.model_name

    def get_embedder(self):
        return self.embedder
