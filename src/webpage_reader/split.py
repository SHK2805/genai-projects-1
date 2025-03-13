from langchain_text_splitters import RecursiveCharacterTextSplitter

class DataSplitter:
    def __init__(self, chunk_size, chunk_overlap):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    def get_chunk_size(self):
        return self.chunk_size

    def get_splitter(self):
        return self.splitter

    def split(self, data):
        return self.splitter.split_documents(data)
