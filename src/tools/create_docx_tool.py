#todo for today April 27th:
#- create a tool that creates a docx file with the given content and title
#- create a tool registry where all tools will be registered and imported from
from langchain.tools import tool
from src.services.document_generator_service import document_generator, DocumentContent, Sections
import logging

logging.basicConfig(level=logging.INFO)

@tool
def create_docx(title: str, content: DocumentContent) -> str:
    """
    A tool that creates a docx file with a given title and context
    
    Args:
        title: The title of the document
        content: [
            { 
                section_heading: "Intoduction",
                section_content: "This is the introduction section of the document" 
            }
        ]
    """

    try:
        if not title or not content:
            logging.error("Title and content are required to create a docx file.")
            return "Error: Title and content are required to create a docx file."
        
        docx = document_generator(title, content)
        
    except Exception as e:
        logging.error(f"Error creating docx file: {e}")
        return f"Error creating docx file: {str(e)}"

    



    

