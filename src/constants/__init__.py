from src.readers.platforms.platform_manager import hf_embedding

openai_llm_model_name:str="o3-mini"
openai_embeddings_model_name:str="text-embedding-ada-002"

ollama_llm_model_name:str="llama3.2"
ollama_embeddings_model_name:str="llama3.2"

hf_embeddings_model_name:str="sentence-transformers/all-mpnet-base-v2"

chunk_size:int=1000
chunk_overlap:int=200