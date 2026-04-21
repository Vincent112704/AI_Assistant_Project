import re 


def preprocess_string(input_string: str) -> str:
    '''
    args: input_string: str - the string to be preprocessed (it should be a raw text so add r"" before the string)
    returns: str - the preprocessed string
    '''
    clean_text = re.sub(r'[^\w\s]', '', input_string)
    return " ".join(clean_text.lower().split())


