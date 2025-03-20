from src.readers.platforms.platform_manager import PlatformManager
from src.utils.common_utils import get_combined_chain
from langchain.chains.retrieval import create_retrieval_chain

class QueryManager:
    def __init__(self, retriever):
        self.retriever = retriever

    def query(self, question, llm, prompt=None):
        """
        Queries the vector store using the provided platform and LLM model.
        :param llm: the LLM model used for question answering.
        :param question: The question to ask.
        :param prompt: The prompt to use.
        """
        # Combine prompt and retriever
        combine_docs_chain = get_combined_chain(llm)
        retrieval_chain = create_retrieval_chain(self.retriever, combine_docs_chain)

        # Ask the question
        response = retrieval_chain.invoke({"input": question})
        return response['answer']
