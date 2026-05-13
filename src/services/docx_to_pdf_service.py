import os
import logging
from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

logging.basicConfig(level=logging.INFO)

def docs_to_pdf(input_docx, output_pdf=None):
    """
    Converts a .docx file to a .pdf file using python-docx + reportlab.

    :param input_docx: Path to the source .docx file
    :param output_pdf: Path for the output .pdf (optional)
    """

    try:

        if not os.path.exists(input_docx):
            logging.error(f"File {input_docx} not found.")
            return {
                "status": "error",
                "message": f"File {input_docx} not found."
            }

        # Default output path
        if output_pdf is None:
            output_pdf = input_docx.replace(".docx", ".pdf")

        # Read DOCX
        doc = Document(input_docx)

        # Create PDF
        pdf = SimpleDocTemplate(output_pdf)
        styles = getSampleStyleSheet()
        elements = []

        # Extract paragraphs
        for para in doc.paragraphs:
            text = para.text.strip()

            if text:
                elements.append(Paragraph(text, styles['BodyText']))
                elements.append(Spacer(1, 12))

        # Build PDF
        pdf.build(elements)

        logging.info(f"Successfully converted {input_docx} to {output_pdf}")

        return {
            "status": "success",
            "path": output_pdf
        }

    except Exception as e:
        logging.error(f"Error converting DOCX to PDF: {e}")

        return {
            "status": "error",
            "message": str(e)
        }