import os

from src.constants import ollama_embeddings_model_name
from src.readers.manager.data_manager import DataManager
from src.readers.services.embedding_service import EmbeddingService
from src.readers.services.vectorstore_service import VectorStoreService
from src.utils.common_utils import get_file_extension
from src.utils.qaenum.embedding_type import EmbeddingTypes


class QAManager:
    def __init__(self, file_path, db_base_path):
        self.file_path = file_path
        self.db_base_path = db_base_path

    def validate_file(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

    def process(self):
        self.validate_file()
        data_manager = DataManager(self.file_path)
        return data_manager.process_text()

    def get_retriever(self,
            embeddings_model_name=ollama_embeddings_model_name,
            embeddings_model_type=EmbeddingTypes.OLLAMA):

        # Determine a database path based on a file type
        file_extension = get_file_extension(self.file_path).lstrip('.')
        faiss_db_path = f"{self.db_base_path}{file_extension}_vector_store"

        try:
            # Process File and Get Documents
            documents = self.process()

            # Get Embeddings
            embedding_service = EmbeddingService()
            embeddings = embedding_service.get_embeddings_model(model_name=embeddings_model_name, model_type=embeddings_model_type)

            # Save or Load Vector Store
            vector_store_service = VectorStoreService(documents, embeddings)
            retriever = vector_store_service.create_vector_store()
            vector_store_service.save_vector_store(faiss_db_path)

            # Load Vector Store (Optional)
            retriever = vector_store_service.load_vector_store(faiss_db_path, embeddings)

            return retriever

        except Exception as e:
            print(f"Error: {e}")
