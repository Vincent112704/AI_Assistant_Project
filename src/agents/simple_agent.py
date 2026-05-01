from src.agents.base_agent import BaseAgent
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent
import logging

logging.basicConfig(level=logging.INFO)
#use langchain for this agent
#while langhraph for the complex agent
class SimpleAgent(BaseAgent):

    def __init__(self, tools=None, memory=None):
        super().__init__(tools, memory)
        self.template = ChatPromptTemplate(
            [("system", "You are a helpful assistant that can use tools to help you complete tasks. "
            "Refer to the following rules of engagement: "
            "1. Do not add any interpretation or assumptions to the user input. Only do what the user explicitly asks you to do."
            "If the user asks you to use a tool, only use the tool and do not add any additional information or context. "
            "2. When a user query is given and you do not have access to the tools needed to accomplish the task, respond with 'I cannot")
            ("human", "{query}")
            ]
        )
        self.agent = create_agent(self.llm, self.tools, self.template)
        



    
    def run(self, query: str) -> str:
        """Executes the agent's main logic. Takes user input and processes it to generate a response."""

        final_state = None

        for chunk in self.agent.stream({
            "messages": [{"role": "user", "content": query}]
        }):
            logging.info(f"Agent response chunk: {chunk}")
            final_state = chunk

        return final_state["messages"][-1]["content"]

    