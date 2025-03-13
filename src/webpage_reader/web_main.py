from src.webpage_reader.constants import openai_embeddings_model_name
from src.webpage_reader.embedding import DataEmbedder

from src.webpage_reader.reader import WebPageReader
from src.webpage_reader.split import DataSplitter
from src.webpage_reader.vectorstore import VectorStore

from src.config.set_config import Config

from langchain_core.prompts import ChatPromptTemplate

config = Config()
if config.set():
    print("Environment variables set")
else:
    print("Environment variables NOT set")

# https://www.sparklebox.co.uk/literacy/nursery-rhymes/lyrics/jack-and-jill/
# https://kids.britannica.com/kids/article/rainbow/400160
reader = WebPageReader(url="https://www.sparklebox.co.uk/literacy/nursery-rhymes/lyrics/jack-and-jill/")
document = reader.read()
# print(document)
splitter = DataSplitter(chunk_size=1000, chunk_overlap=200)
documents = splitter.split(document)
# print(*documents, sep="\n")
embeddings = DataEmbedder(model_name=openai_embeddings_model_name).get_embedder()
vectorstore = VectorStore(documents, embeddings)
query = "Jack and Jill went up the hill"
results = vectorstore.similarity_search(query)
# print(*results, sep="\n")
# print(results[0].page_content)

prompt = ChatPromptTemplate.from_template(
"""
Answer the following questions based only on the provided context:
<context>
{context}
</context>
"""
)




