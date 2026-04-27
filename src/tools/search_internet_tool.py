from langchain.tools import tool
from dotenv import load_dotenv
import os
from langchain_community.utilities import GoogleSerperAPIWrapper
import logging

logging.basicConfig(level=logging.INFO)
load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SerperWrapper = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)


@tool
def search_internet(query: str) -> str:
    """
    Searches the internet for a given query and returns the result of the query
    
    Args: 
        query: The query to seaarch for on the internet
    Returns:
        The result of the query
    
    """
    result = SerperWrapper.run(query) # might have to parse this depending on how llm passes input
    return result
    
# if you want to test the tool independently, remove te @tool decorator and uncomment the code below
# test = search_internet("What is the capital of France?")
# print(test) 
