import string

def remove_punctuation(filtrated_words_list):
    # Create a translator to remove punctuation
    translator = str.maketrans('', '', string.punctuation)

    punc_removed_list = []
    for sentence in filtrated_words_list:
        punc_removed_sentence = [word.translate(translator) for word in sentence]
        punc_removed_list.append(punc_removed_sentence)

    return punc_removed_list