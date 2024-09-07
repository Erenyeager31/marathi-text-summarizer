import re

def filter_devanagari(tokenized_words_list):
    # Regular expression pattern for English words (to remove non-Devanagari words)
    english_pattern = re.compile(r'\b[a-zA-Z]+\b')

    # Filter each sentence in the tokenized list
    filtered_list = []
    for sentence in tokenized_words_list:
        filtered_sentence = [word for word in sentence if not english_pattern.fullmatch(word)]
        filtered_list.append(filtered_sentence)

    return filtered_list  # Return list of filtered tokenized words