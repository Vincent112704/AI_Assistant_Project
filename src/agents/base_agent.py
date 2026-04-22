from abc import ABC, abstractmethod
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#todo 
#verify if the LLM is instantiated 
#add langsmith for tracing
#add simple and complex agent
#add and integrate the tools 
#create prompt templates for each agent


class BaseAgent(ABC):

    def __init__(self, tools=None, memory=None):

        self.llm = self._initialize_llm()
        self.tools = tools or []
        self.memory = memory

    def _initialize_llm(self):
        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0, 
        )

    def get_tools(self):
        return self.tools

    def add_tool(self, tool):
        self.tools.append(tool)

    @abstractmethod
    def run(self, user_input: str):
        """
        Main execution method.
        Each agent state implements its own behavior.
        """
        pass