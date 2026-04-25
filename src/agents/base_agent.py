from abc import ABC, abstractmethod
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

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
            api_key=OPENAI_API_KEY
        )

    def get_tools(self):
        return self.tools

    def add_tool(self, tool):
        self.tools.append(tool) # Might have to change this so that all agents have access to the same tools instead of each agent having its own set of tools

    @abstractmethod
    def run(self, user_input: str):
        """
        Main execution method.
        Each agent state implements its own behavior.
        """
        pass