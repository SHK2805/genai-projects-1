from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from src.config.set_config import Config

class LegendaryCreatureTool:
    def __init__(self, url: str,
                 chunk_size: int = 1000,
                 chunk_overlap: int = 200):
        self.url = url
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def set_environment(self) -> bool:
        config = Config()
        return config.set()

    def create_tool(self):
        if self.set_environment():
            print("Environment variables set")
        else:
            print("Environment variables NOT set")
        # Load and split documents
        loader = WebBaseLoader(self.url)
        docs = loader.load()
        documents = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        ).split_documents(docs)

        # Create vector store and retriever
        db = FAISS.from_documents(documents, OpenAIEmbeddings())
        retriever = db.as_retriever()

        # Create the retriever tool
        retriever_tool = create_retriever_tool(
            retriever,
            "legendary_creature", # should match the pattern '^[a-zA-Z0-9_-]+$'."
            "This describes legendary creatures from Wikipedia"
        )
        return retriever_tool

