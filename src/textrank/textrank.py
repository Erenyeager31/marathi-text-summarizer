import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.utils.preprocess import preprocess
from src.tf_idf.td_idf import highlight_original_text,summarize_with_highlighted_synonyms,replace_synonyms
from src.data.synonyms import synonym_dict

def summarize_text_textrank(paragraph, num_sentences=4):
    # Preprocess and tokenize the input text
    processed_text = preprocess(paragraph.title())
    sentences = [' '.join(sentence) for sentence in processed_text]
    
    # Create TF-IDF matrix
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    
    # Compute similarity matrix
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Create graph and apply PageRank
    graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(graph)
    
    # Rank sentences
    ranked_sentences = sorted(((scores[i], i) for i in range(len(sentences))), reverse=True)
    
    # Select top sentences
    top_sentences_idx = [idx for _, idx in ranked_sentences[:num_sentences]]
    top_sentences_idx = sorted(top_sentences_idx)
    
    # Create the summarized text
    summarized_text = " ".join([sentences[idx] + "." for idx in top_sentences_idx])

    # Replace synonyms in the summarized text and track replaced words
    summarized_text_with_synonyms, replaced_words = replace_synonyms(summarized_text, synonym_dict)

    # Highlight the synonyms in the summarized text
    highlighted_summarized_text = summarize_with_highlighted_synonyms(summarized_text_with_synonyms, replaced_words)
    
    # Highlight sentences in the original text
    highlighted_original_text = highlight_original_text(sentences, top_sentences_idx, replaced_words)
    
    return highlighted_summarized_text, highlighted_original_text

# Use the same helper functions as in the original code:
# summarize_with_highlighted_synonyms, highlight_original_text, replace_synonyms