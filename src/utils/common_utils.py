from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


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
    system_prompt = """Answer the following question based ONLY on the provided context. Do not use any external information. Don't worry if you don't know the answer. Just say I don't know. Do not hallucinate or make up information. Only answer based on the provided context.:
    <context>
    {context}
    </context>"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])
    return prompt

def get_combined_chain(llm_model_name):
    # prompt the question
    prompt = get_message_prompt()
    # create the chain
    llm = ChatOpenAI(model=llm_model_name)
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    return combine_docs_chain