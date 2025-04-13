from src.config.set_config import Config
from src.constants import *
from src.readers.manager.query_manager import QueryManager
from src.readers.manager.vectorstore_manager import VectorStoreManager
from src.readers.platforms.paltform_types import PlatformTypes
from src.readers.platforms.platform_manager import PlatformManager


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

    # Initialize QAManager for file processing and retriever creation
    vectorstore_manager = VectorStoreManager(file_path, db_base_path)

    try:
        # Initialize PlatformManager
        platform_manager = PlatformManager(PlatformTypes.OPENAI)
        llm = platform_manager.get_llm(openai_llm_model_name)
        embedding = platform_manager.get_embedding(openai_embeddings_model_name)

        # Get the retriever Vectorstore
        retriever = vectorstore_manager.get_retriever(embeddings=embedding)

        # Initialize QueryManager with the retriever
        query_manager = QueryManager(retriever)

        # Query the data using QueryManager
        question = "Where are the most famous Egyptian pyramids found?"
        answer = query_manager.query(
            question=question,
            llm=llm
        )

        # Print the result
        print(f"Question: {question}")
        print(f"Answer: {answer}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
