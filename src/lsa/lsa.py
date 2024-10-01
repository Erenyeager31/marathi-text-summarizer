import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from src.utils.preprocess import preprocess
from src.tf_idf.td_idf import highlight_original_text, summarize_with_highlighted_synonyms, replace_synonyms
from src.data.synonyms import synonym_dict

def summarize_text_lsa(paragraph, num_sentences=4):
    # Preprocess and tokenize the input text
    processed_text = preprocess(paragraph.title())
    sentences = [' '.join(sentence) for sentence in processed_text]

    # Create TF-IDF matrix
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    
    # Perform LSA
    lsa = TruncatedSVD(n_components=min(num_sentences, len(sentences) - 1), algorithm='randomized', random_state=42)
    lsa_scores = lsa.fit_transform(tfidf_matrix)

    # Calculate the scores for each sentence
    sentence_scores = np.sum(lsa_scores, axis=1)

    # Select top sentences based on their scores
    top_sentences_idx = np.argsort(sentence_scores)[-num_sentences:][::-1]  # Get the indices of the top sentences
    top_sentences_idx = sorted(top_sentences_idx)  # Sort to maintain the original order

    # Create the summarized text
    summarized_text = " ".join([sentences[idx] + "." for idx in top_sentences_idx])
    
    # Replace synonyms in the summarized text and track replaced words
    summarized_text_with_synonyms, replaced_words = replace_synonyms(summarized_text, synonym_dict)

    # Highlight the synonyms in the summarized text
    highlighted_summarized_text = summarize_with_highlighted_synonyms(summarized_text_with_synonyms, replaced_words)

    # Highlight sentences in the original text
    highlighted_original_text = highlight_original_text(sentences, top_sentences_idx, replaced_words)
    
    return highlighted_summarized_text, highlighted_original_text