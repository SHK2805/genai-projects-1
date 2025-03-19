from src.config.set_config import Config
from src.readers.manager.qa_manager import QAManager
from src.readers.manager.query_manager import QueryManager



def main():
    # Set Environment Configurations
    config = Config()
    if config.set():
        print("Environment variables set")
    else:
        print("Environment variables NOT set")

    # File Path and Database Path
    file_path = "../../data/pyramids.pdf"  # Update to the desired file
    db_base_path = "../../database/"

    # Initialize File Manager
    qa_manager = QAManager(file_path, db_base_path)

    try:
        retriever = qa_manager.run()

        # Query the Data
        query_manager = QueryManager(retriever)
        answer = query_manager.query("Where are the most famous Egyptian pyramids found ?")
        print(answer)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
