from pathlib import Path
from uuid import uuid4

from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader, Docx2txtLoader
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from src.config.set_config import Config
from src.constants import *

load_dotenv()

config = Config()
if config.set():
    print("Environment variables set")
else:
    print("Environment variables NOT set")

def get_file_extension(file_path:str):
    # os.path.splitext(file_path)[1].lower()
    return Path(file_path).suffix.lower()

def get_document_map():
    return {
        ".txt": TextLoader,
        ".csv": CSVLoader,
        ".xls": UnstructuredExcelLoader,
        ".xlsx": UnstructuredExcelLoader,
        ".docx": Docx2txtLoader,
        ".doc": Docx2txtLoader,
        ".pdf": PyPDFLoader,
    }

def get_loader(file_path, mapping=None):
    if mapping is None:
        mapping = get_document_map()
    ext = get_file_extension(file_path)
    loader = mapping.get(ext)
    if not loader:
        raise ValueError(f"Unsupported file type: {ext}")
    return loader(file_path)

def get_template_prompt():
    # Define a prompt template for question answering
    system_prompt = """Answer the following question based ONLY on the provided context. Do not use any external information. Don't worry if you don't know the answer. Just say I don't know. Do not hallucinate or make up information. Only answer based on the provided context.:
    <context>
    {context}
    </context>"""

    prompt = ChatPromptTemplate.from_template(system_prompt)
    return prompt

def get_message_prompt():
    # Define a prompt template for question answering
    system_prompt = """Answer the following question based ONLY on the provided context. Do not use any external information. Don't worry if you don't know the answer. Do not hallucinate or make up information. Only answer based on the provided context.:
    <context>
    {context}
    </context>"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])
    return prompt

def get_openai_embeddings(embeddings_model_name=openai_embeddings_model_name):
    """Fetches OpenAI embeddings based on the provided model name."""
    return OpenAIEmbeddings(model=embeddings_model_name)

def get_ollama_embeddings(embeddings_model_name=ollama_embeddings_model_name):
    """Fetches Ollama embeddings based on the provided model name."""
    return OllamaEmbeddings(model=embeddings_model_name)

def get_openai_llm_model(llm_model_name = openai_llm_model_name):
    """Fetches OpenAI llm based on the provided model name."""
    return ChatOpenAI(model=llm_model_name)

def get_ollama_llm_model(llm_model_name = ollama_llm_model_name):
    """Fetches Ollama llm based on the provided model name."""
    return OllamaLLM(model=llm_model_name)

def get_uuids(docs_len):
    return [str(uuid4()) for _ in range(docs_len) if docs_len > 0]

def get_combined_chain(llm, prompt=get_message_prompt()):
    """Creates a combined chain using the specified LLM model and prompt."""
    if llm is None:
        raise ValueError("LLM model cannot be None")

    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    return combine_docs_chain




