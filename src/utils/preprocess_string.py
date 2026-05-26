import logging
import re 

logging.basicConfig(level=logging.INFO)

def preprocess_string(input_string: str) -> str:
    '''
    args: input_string: str - the string to be preprocessed (it should be a raw text so add r"" before the string)
    returns: str - the preprocessed string

    This removes all punctuation and special characters from the input string, converts it to lowercase, and .
    It removes contractions like "don't" to "dont" and possessives like "John's" to "Johns".
    which could lead to misinterpretation by the LLM.
    '''
    clean_text = re.sub(r'[^\w\s]', '', input_string)
    logging.info(f"Preprocessed text: {clean_text}")
    return " ".join(clean_text.lower().split())


