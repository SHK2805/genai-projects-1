import os
import shutil

from langchain_community.vectorstores import FAISS

class VectorStoreService:
    def __init__(self, documents=None, embeddings=None):
        self.documents = documents
        self.embeddings = embeddings
        self.vector_store = None

    def create_vector_store(self):
        if self.documents and self.embeddings:
            self.vector_store = FAISS.from_documents(self.documents, self.embeddings)
        else:
            raise ValueError("Documents and embeddings must be provided to create the vector store.")
        return self.vector_store.as_retriever()

    def save_vector_store(self, file_path):
        if self.vector_store:
            # delete the existing folder if it exists
            if os.path.exists(file_path):
                shutil.rmtree(file_path)
                print(f"Deleted existing FAISS database at: {file_path}")
            self.vector_store.save_local(file_path)
            print(f"FAISS database saved to: {file_path}")
        else:
            raise RuntimeError("Vector store has not been created.")

    def load_vector_store(self, file_path, embeddings):
        self.vector_store = FAISS.load_local(
            file_path, embeddings, allow_dangerous_deserialization=True
        )
        print(f"FAISS database loaded from: {file_path}")
        return self.vector_store.as_retriever()
