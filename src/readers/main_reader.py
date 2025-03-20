from src.config.set_config import Config
from src.constants import ollama_embeddings_model_name, ollama_llm_model_name
from src.readers.manager.qa_manager import QAManager
from src.readers.manager.query_manager import QueryManager
from src.readers.services.llm_service import LLMModelService
from src.utils.qaenum.embedding_type import EmbeddingTypes
from src.utils.qaenum.model_type import LLMTypes


def main():
    # Set Environment Configurations
    config = Config()
    if config.set():
        print("Environment variables set")
    else:
        print("Environment variables NOT set")

    # File Path and Database Path
    file_path = "../../data/pyramids.txt"  # Update to the desired file
    db_base_path = "../../database/"


    # Initialize File Manager
    qa_manager = QAManager(file_path, db_base_path)

    try:
        embeddings_model_name = ollama_embeddings_model_name
        embeddings_model_type = EmbeddingTypes.OLLAMA
        retriever = qa_manager.get_retriever(embeddings_model_name=embeddings_model_name, embeddings_model_type=embeddings_model_type)

        # Query the Data
        llm_model_name = ollama_llm_model_name
        llm_model_type = LLMTypes.OLLAMA
        llm_model_service = LLMModelService(llm_model_type)
        query_manager = QueryManager(retriever)
        answer = query_manager.query("Where are the most famous Egyptian pyramids found ?",
                                     None,
                                     llm_model_name,
                                     llm_model_service)
        print(answer)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
