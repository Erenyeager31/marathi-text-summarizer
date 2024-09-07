from src.utils.sent_tokenize import sent_tokenize
from src.utils.word_tokenize import word_tokenize
from src.utils.lemmatize_words import lemmatize_tokenized_words
from src.utils.stopword_remover import remove_stopwords
from src.utils.filtration import filter_devanagari
from src.utils.remove_punctuation import remove_punctuation

def preprocess(paragraph:str):
    # sentence-tokeniation
    tokenized_sentences = sent_tokenize(paragraph)
    # return tokenized_sentences

    # word-tokenization
    tokenized_words = word_tokenize(tokenized_sentences)
    # return tokenized_words

    # lemmatization
    lemmatized_word_op = lemmatize_tokenized_words(tokenized_words)
    # return lemmatized_word_op

    # stop words removal
    stopword_removed = remove_stopwords(lemmatized_word_op)
    # return stopword_removed

    # filtration
    filtration_op = filter_devanagari(stopword_removed)
    # return filtration_op

    # scrip validation
    punc_processed = remove_punctuation(filtration_op)
    return punc_processed