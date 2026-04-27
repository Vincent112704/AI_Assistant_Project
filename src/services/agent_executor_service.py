from src.services.query_classifier_service import classify_query
from src.agents.simple_agent import SimpleAgent
from src.tools.search_internet_tool import search_internet
import logging

logging.basicConfig(level=logging.INFO)

"""
Planned simple agent architecture:
    - will not have reasoning 
    - will be do what is told to do 
    - does not plan

Input -> LLM reads input -> chooses tool -> executes tool -> [format output if necessary] -> returns output to telegram 

"""

def execute_agent(query: str) -> str:
    try:
        query_classification = classify_query(query)
        logging.info(f"Query classified as: {query_classification}")

        if query_classification == "simple":
            agent = SimpleAgent(tools=[search_internet])
            result = agent.run(query)
            return result
        #elif query_classification == "complex":
            #run complex agent
        #else: do something about the unknown classification returned (i don't know yet)
        

    except Exception as e:
        logging.error(f"Error executing agent: {e}")
        return f"Error executing agent: {str(e)}"