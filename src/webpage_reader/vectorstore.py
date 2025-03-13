from langchain_community.vectorstores import FAISS
from src.webpage_reader.embedding import DataEmbedder

class VectorStore:
    def __init__(self, documents, embedder=None):
        self.embedder = embedder
        self.vectorstore = FAISS.from_documents(documents, self.embedder)

    def get_vectorstore(self):
        return self.vectorstore

    def get_embedder(self):
        return self.embedder

    def similarity_search(self, query, k=4):
        return self.vectorstore.similarity_search(query, k)
