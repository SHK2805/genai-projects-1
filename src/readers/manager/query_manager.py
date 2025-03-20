from langchain.chains.retrieval import create_retrieval_chain

from src.constants import openai_llm_model_name
from src.utils.common_utils import get_combined_chain
from src.utils.qaenum.model_type import LLMTypes


class QueryManager:
    def __init__(self, retriever):
        self.retriever = retriever

    def query(self,
              question,
              prompt,
              llm_model_name,
              llm_model_service):
        # Get the combined chain
        combine_docs_chain = get_combined_chain(llm_model_name=llm_model_name,
                                                model_service=llm_model_service,
                                                prompt=prompt)
        retrieval_chain = create_retrieval_chain(self.retriever, combine_docs_chain)

        # Ask the question
        response = retrieval_chain.invoke({"input": question})
        return response['answer']