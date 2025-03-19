from src.config.set_config import Config
from src.readers.manager.data_manager import DataManager
from src.readers.manager.query_manager import QueryManager
from src.readers.services.embedding_service import EmbeddingService
from src.readers.services.vectorstore_service import VectorStoreService


def main():
    # Set Environment Configurations
    config = Config()
    if config.set():
        print("Environment variables set")
    else:
        print("Environment variables NOT set")

    # File Path
    txt_file_path = "../../data/pyramids.txt"
    txt_faiss_db_path = "../../database/txt_vector_store"

    data_manager = DataManager(txt_file_path)
    embedding_service = EmbeddingService()

    # Save or Load Vector Store
    try:
        # To create and save the vector store
        documents = data_manager.process_text()
        embeddings = embedding_service.get_embeddings()
        vector_store_service = VectorStoreService(documents, embeddings)
        retriever = vector_store_service.create_vector_store()
        vector_store_service.save_vector_store(txt_faiss_db_path)

        # To load an existing vector store
        retriever = vector_store_service.load_vector_store(txt_faiss_db_path, embeddings)

        # Query the data
        query_manager = QueryManager(retriever)
        answer = query_manager.query("How many pyramids were constructed in the Kingdom of Kush?")
        print(answer)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
