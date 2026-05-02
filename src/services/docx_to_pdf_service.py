from docx2pdf import convert
import os
import logging

logging.basicConfig(level=logging.INFO)

def docs_to_pdf(input_docx, output_pdf=None):
    """
    Converts a .docx file to a .pdf file.
    
    :param input_docx: Path to the source .docx file
    :param output_pdf: Path for the output .pdf (optional)
    """
    try:
        
        if not os.path.exists(input_docx):
            logging.error(f"File {input_docx} not found.")
            return {"status": "error", "message": f"File {input_docx} not found."}

        
        convert(input_docx, output_pdf)

        logging.info(f"Successfully converted {input_docx} to {output_pdf or input_docx.replace('.docx', '.pdf')}")
        return {"status": "success", "path": output_pdf or input_docx.replace(".docx", ".pdf")}
    
    except Exception as e:
        logging.error(f"Error converting DOCX to PDF: {e}")
        return {"status": "error", "message": str(e)}
    

#Still have to do unit tests for this, too lazy right now