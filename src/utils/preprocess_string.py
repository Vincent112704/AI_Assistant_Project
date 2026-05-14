import logging
import re 

logging.basicConfig(level=logging.INFO)

def preprocess_string(input_string: str) -> list:
    '''
    args: input_string: str - the string to be preprocessed (it should be a raw text so add r"" before the string)
    returns: list - the preprocessed string as a list of words
    '''
    clean_text = re.sub(r'[^\w\s]', '', input_string)
    logging.info(f"Preprocessed text: {clean_text}")
    return " ".join(clean_text.lower().split())


