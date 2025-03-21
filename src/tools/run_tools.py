from langchain import hub
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_openai import ChatOpenAI

from src.constants import openai_llm_model_name
from src.tools.custom_tools import LegendaryCreatureTool


class RunTools:
    def __init__(self):
        pass

    def get_arxiv(self):
        api_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=100)
        tool = ArxivQueryRun(api_wrapper=api_wrapper)
        return tool

    def get_wikipedia(self):
        api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
        tool = WikipediaQueryRun(api_wrapper=api_wrapper)
        return tool

    def get_legendary_creature(self):
        retriever_tool_creator = LegendaryCreatureTool("https://en.wikipedia.org/wiki/Legendary_creature")
        tool = retriever_tool_creator.create_tool()
        return tool

# usage
if __name__ == "__main__":
    run_tools = RunTools()
    wikipedia_tool = run_tools.get_wikipedia()
    # print(wikipedia_query_run.run("Trump"))
    arxiv_tool = run_tools.get_arxiv()
    # print(arxiv_query_run.run("Trump"))
    retriever_tool = run_tools.get_legendary_creature()

    tools = [wikipedia_tool, arxiv_tool, retriever_tool]
    prompt = hub.pull("hwchase17/openai-functions-agent") # https://smith.langchain.com/hub/hwchase17/openai-functions-agent
    llm = ChatOpenAI(model=openai_llm_model_name)
    agent = create_openai_tools_agent(llm, tools, prompt)

    executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    # response = executor.invoke({"input": "What is a Phoenix?"}) # fetches from our custom tool retriever
    response = executor.invoke({"input": "1706.03762"}) # fetches from arxiv
    print(response['output'])

