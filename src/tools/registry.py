"""
A library of all tools available to the agents. 
This is where all tools will be registered and imported from. 
This describes the tool, the parameters it takes, and the output it returns.
This way, we can easily manage and update the tools available to the agents in one place.
"""

from src.tools.search_internet_tool import search_internet
from src.tools.create_docx_tool import create_docx
import logging

logging.basicConfig(level=logging.INFO)

TOOL_MAPPING = {
    "search_internet": search_internet,
}

