import pandas as pd
from indicnlp.tokenize import indic_tokenize

def word_tokenize(sentences: list):
    # Tokenize each sentence into words
    word_tokenized_list = []
    
    for sentence in sentences:
        output = list(indic_tokenize.trivial_tokenize(sentence, lang='mr'))
        word_tokenized_list.append(output)
    return word_tokenized_list