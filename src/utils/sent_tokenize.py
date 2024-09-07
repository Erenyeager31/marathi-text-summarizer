import pandas as pd
from indicnlp.tokenize import sentence_tokenize

def sent_tokenize(paragraph:str):
    tokenized_sentences = sentence_tokenize.sentence_split(paragraph, lang='mr')
    
    return tokenized_sentences
