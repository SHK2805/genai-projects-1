import os
from src.readers.services.data_loader_service import DataLoader
from src.constants import chunk_size, chunk_overlap

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def validate_file(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

    def process_text(self):
        """
        Load the text file, split it into chunks, and generate unique identifiers.
        """
        self.validate_file()
        processor = DataLoader(self.file_path)
        split_docs = processor.load_and_split_text(size=chunk_size, overlap=chunk_overlap)

        if not split_docs:
            raise ValueError("No chunks were generated. Ensure the text file is not empty or misconfigured.")

        print(f"Text processed into {len(split_docs)} chunks.")
        return split_docs
