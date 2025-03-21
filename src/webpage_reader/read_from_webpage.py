from src.config.set_config import Config
from src.utils.common_utils import get_combined_chain
from src.webpage_reader.constants import *

config = Config()
if config.set():
    print("Environment variables set")
else:
    print("Environment variables NOT set")

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import create_retrieval_chain

class WebPageQA:
    def __init__(self, url = "https://en.wikipedia.org/wiki/Legendary_creature",
                 llm_model_name = openai_llm_model_name,
                 embeddings_model_name = openai_embeddings_model_name):
        self.url = url
        self.llm_model_name = llm_model_name
        self.embeddings_model_name = embeddings_model_name

    def init(self):
        # read the text from the webpage
        loader = WebBaseLoader(self.url)
        docs = loader.load()
        # split the text into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        split_docs = splitter.split_documents(docs)
        # get the embeddings for each chunk
        embeddings = OpenAIEmbeddings(model=self.embeddings_model_name)
        # create the vector store
        vectorstore = FAISS.from_documents(split_docs, embeddings)
        retriever = vectorstore.as_retriever()
        return retriever

    def ask(self, retriever, question):
        combine_docs_chain = get_combined_chain(self.llm_model_name)
        retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)
        # invoke the chain with the query
        response = retrieval_chain.invoke({"input": question})
        return response['answer']

    def run(self):
        retriever = self.init()
        answer = self.ask(retriever, "What is a legendary creature?")
        print(answer)

if __name__ == "__main__":
    qa = WebPageQA()
    qa.run()