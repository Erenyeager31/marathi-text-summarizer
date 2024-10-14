# import math
# from collections import defaultdict

# # Step 1: Term Frequency (TF)
# def compute_tf(word_list):
#     tf_dict = {}
#     total_words = len(word_list)
    
#     for word in word_list:
#         tf_dict[word] = tf_dict.get(word, 0) + 1
    
#     # Normalize by the number of words in the sentence
#     for word in tf_dict:
#         tf_dict[word] /= total_words
    
#     return tf_dict

# # Step 2: Inverse Document Frequency (IDF)
# def compute_idf(processed_text):
#     num_sentences = len(processed_text)
#     idf_dict = defaultdict(int)
    
#     # Count the number of sentences containing each word
#     for sentence in processed_text:
#         for word in set(sentence):  # Using set to count only once per sentence
#             if word:
#                 idf_dict[word] += 1
    
#     # Calculate the IDF for each word
#     for word in idf_dict:
#         idf_dict[word] = math.log(num_sentences / float(idf_dict[word]))
    
#     return idf_dict

# # Step 3: TF-IDF Calculation
# def compute_tf_idf(tf_dict, idf_dict):
#     tf_idf_dict = {}
    
#     for word, tf_value in tf_dict.items():
#         tf_idf_dict[word] = tf_value * idf_dict.get(word, 0)
    
#     return tf_idf_dict

# # Step 4: Putting it all together
# def tf_idf(processed_text):
#     idf_dict = compute_idf(processed_text)
    
#     tf_idf_scores = []
#     for sentence in processed_text:
#         tf_dict = compute_tf(sentence)
#         tf_idf_dict = compute_tf_idf(tf_dict, idf_dict)
#         tf_idf_scores.append(tf_idf_dict)
    
#     return tf_idf_scores

#? 1st iter
import math
from collections import defaultdict
from src.utils.preprocess import preprocess
from src.utils.replace_synonyms import replace_synonyms

synonym_dict = {
    'अवसर': 'संधी',
    'सदन': 'भवन',
    'व्रत': 'उपास',
    'मुली': 'कन्या',
    'शेत': 'कृषी',
    'दूर': 'लांब',
    'नाव': 'नाम',
    'सपनों': 'स्वप्न',
    'शेण': 'गोमूत्र',
    'माल': 'संपत्ती',
    'नमस्कार': 'सुप्रभात',
    'काम': 'उद्योग',
    'खोल': 'आकर्षक',
    'विद्यार्थी': 'शिक्षार्थी',
    'पार्क': 'उद्यान',
    'अधिकार': 'अधिकार',
    'जन्म': 'उत्पत्ती',
    'माहात्म्य': 'महत्त्व',
    'संपूर्ण': 'पूर्ण',
    'पुंड': 'धन',
    'मास': 'महिना',
    'जंगल': 'वन',
    'चांगले': 'उत्कृष्ट',
    'खूप': 'अधिक',
    'भांडण': 'विवाद',
    'अवशेष': 'अवशेष',
    'स्मरण': 'याद',
    'वातावरण': 'अंग',
    'नरेंद्र': 'राजा',
    'समारंभ': 'उत्सव',
    'वायू': 'हवा',
    'शिकारी': 'शिकार',
    'अशी': 'समान',
    'संसार': 'जीवन',
    'दुःख': 'कंटक',
    'साधन': 'उपकरण',
    'परे': 'दूर',
    'चाल': 'गती',
    'लक्ष्य': 'उद्दीष्ट',
    'कथा': 'कहानी',
    'गृहनिर्माण': 'घर',
    'अभ्यास': 'शिक्षण',
    'उत्सव': 'अभिनंदन',
    'दुरुस्त': 'सुधारित',
    'प्रारंभ': 'सुरूवात',
    'प्रेरणा': 'उत्साह',
    'चुक': 'असफलता',
    'शोभा': 'सौंदर्य',
    'शाळा': 'विद्यापीठ',
    'आयकर': 'कर',
    'चिंता': 'आत्ममंथन',
    'मला': 'माझे',
    'ज्ञान': 'अभ्यास',
      'पुस्तक': 'ग्रंथ',
    'शांत': 'निःशब्द',
    'प्रकाश': 'उजेड',
    'मित्र': 'सखा',
    'स्त्री': 'महिला',
    'पुरुष': 'माणूस',
    'समाधान': 'तृप्ती',
    'विजय': 'जिंकणे',
    'पराभव': 'हार',
    'शक्ती': 'बल',
    'सुरुवात': 'आरंभ',
    'समाप्त': 'अंत',
    'भूख': 'क्षुधा',
    'पाणी': 'जल',
    'अन्न': 'भोजन',
    'विचार': 'ध्यान',
    'शिकवण': 'धडा',
    'सत्य': 'खरे',
    'आनंद': 'सुख',
    'दुःख': 'वेदना',
    'प्रेम': 'माया',
    'आसक्ती': 'तळमळ',
    'परिवर्तन': 'बदल',
    'गुण': 'वैशिष्ट्य',
    'अवघड': 'कठीण',
    'सोपी': 'सुगम',
    'संपर्क': 'संबंध',
    'नियोजन': 'योजना',
    'कर्तव्य': 'जबाबदारी',
    'सर्व': 'संपूर्ण',
    'आकर्षण': 'प्रभाव',
    'दु:ख': 'वेदना',
    'क्षण': 'क्षणभंगुर',
    'बोलणे': 'संवाद',
    'शिकवणे': 'शिक्षण',
    'विज्ञान': 'शास्त्र',
    'आरोग्य': 'स्वास्थ्य',
    'समस्या': 'अडचण',
    'समाधान': 'तृप्ती',
    'कारण': 'हेतु',
    'परिणाम': 'निष्कर्ष',
    'इच्छा': 'आकांक्षा',
    'शांती': 'सुव्यवस्था',
    'पर्वत': 'डोंगर',
    'नदी': 'सरिता',
    'सूर्य': 'रवी',
    'चंद्र': 'शशी',
    'आकाश': 'गगन',
    'जागा': 'स्थान',
    'तैलचित्र': 'चित्रकला',
    'अधिकारी': 'जबाबदार',
    'वास्तववाद': 'सत्य',
    'अधिकृत': 'वैध',
    'यश': 'सफलता',
    'स्मरण': 'याद',
    'लोककला': 'जनकला',
    'यशस्वी': 'सफल',
    'सरकारी': 'प्रशासकीय',
    'कलाकार': 'चित्रकार'
}

def summarize_text(paragraph,num_sentences):
    # Preprocess and tokenize the input text
    processed_text = preprocess(paragraph.title())
    sentences = [' '.join(sentence) for sentence in processed_text]
    
    # Calculate TF-IDF scores
    tf_idf_scores = compute_tf_idf_scores(processed_text)
    
    sentence_scores = []
    for idx, sentence_scores_dict in enumerate(tf_idf_scores):
        sentence_total_score = sum(sentence_scores_dict.values())
        sentence_scores.append((idx, sentence_total_score))
    
    sentence_scores.sort(key=lambda x: x[1], reverse=True)
    
    # Select top 4 sentences for summarization
    top_sentences_idx = [idx for idx, score in sentence_scores[:num_sentences]]
    top_sentences_idx.sort()
    
    # Create the summarized text
    summarized_text = " ".join([sentences[idx] + "." for idx in top_sentences_idx])

    # Replace synonyms in the summarized text and track replaced words
    summarized_text_with_synonyms, replaced_words = replace_synonyms(summarized_text, synonym_dict)

    # Highlight the synonyms in the summarized text
    highlighted_summarized_text = summarize_with_highlighted_synonyms(summarized_text_with_synonyms, replaced_words)
    
    # Highlight sentences in the original text
    highlighted_original_text = highlight_original_text(sentences, top_sentences_idx, replaced_words)
    
    return highlighted_summarized_text, highlighted_original_text

def summarize_with_highlighted_synonyms(summarized_text, replaced_words):
    for original, synonym in replaced_words.items():
        summarized_text = summarized_text.replace(synonym, f"<span style='background-color: blue; color: white;'>{synonym}</span>")
    return summarized_text

def highlight_original_text(sentences, top_sentences_idx, replaced_words):
    highlighted_text = ""
    for idx, sentence in enumerate(sentences):
        if idx in top_sentences_idx:
            # Highlight selected sentences in yellow
            highlighted_sentence = f"<span style='background-color: yellow; color:black; font-style:italic;'>{sentence}.</span> "
            
            # Further highlight any synonym-replaced words in blue
            for original, synonym in replaced_words.items():
                highlighted_sentence = highlighted_sentence.replace(synonym, f"<span style='background-color: blue; color: white;'>{synonym}</span>")
            
            highlighted_text += highlighted_sentence
        else:
            highlighted_text += f"{sentence}. "
    
    return highlighted_text

def compute_tf(word_list):
    tf_dict = {}
    total_words = len(word_list)
    
    for word in word_list:
        tf_dict[word] = tf_dict.get(word, 0) + 1
    
    # Normalize by the number of words in the sentence
    for word in tf_dict:
        tf_dict[word] /= total_words
    
    return tf_dict

def compute_idf(processed_text):
    num_sentences = len(processed_text)
    idf_dict = defaultdict(int)
    
    # Count the number of sentences containing each word
    for sentence in processed_text:
        for word in set(sentence):  # Using set to count only once per sentence
            if word:
                idf_dict[word] += 1
    
    # Calculate the IDF for each word
    for word in idf_dict:
        idf_dict[word] = math.log(num_sentences / float(idf_dict[word]))
    
    return idf_dict

def compute_tf_idf_scores(processed_text):
    idf_dict = compute_idf(processed_text)
    
    tf_idf_scores = []
    for sentence in processed_text:
        tf_dict = compute_tf(sentence)
        tf_idf_dict = {word: tf_value * idf_dict.get(word, 0) for word, tf_value in tf_dict.items()}
        tf_idf_scores.append(tf_idf_dict)
    
    return tf_idf_scores

def replace_synonyms(text: str, synonym_dict: dict):
    words = text.split()
    replaced_words = {}
    
    # Replace words with synonyms and track replaced words
    replaced_text = []
    for word in words:
        synonym = synonym_dict.get(word)
        if synonym:
            replaced_words[word] = synonym
            replaced_text.append(synonym)
        else:
            replaced_text.append(word)
    
    return ' '.join(replaced_text), replaced_words
