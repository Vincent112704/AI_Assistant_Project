from src.agents.base_agent import BaseAgent
import logging

logging.basicConfig(level=logging.INFO)
#use langchain for this agent
#while langhraph for the complex agent
class SimpleAgent(BaseAgent):
    def __init__(self, tools=None, memory=None):
        super().__init__(tools, memory)

    