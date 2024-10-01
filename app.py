# # import the required modules
# import streamlit as st
# import time
# from src.utils.preprocess import preprocess
# from src.tf_idf.td_idf import tf_idf
# from src.utils.replace_synonyms import replace_synonyms

# # UI code

# # set the title of the page
# st.set_page_config(
#     page_title='मराठी Text-Summarizer'
# )

# # set header for the page
# st.header('Welcome to the मराठी Text-Summarizer')

# # input elements
# st.subheader('')
# paragraph = st.text_area(
#     "Enter the text you want to summarize",
#     height=200
# )

# # button for submitting input
# submitButton = st.button(
#     label="Summarize"
# )

# # functionality on submit
# if(submitButton):
#     if(paragraph.title() == ""):
#         st.markdown(
#             f'<p style="color: red; font-style: italic; font-weight:900;">No text provided</p>',
#             unsafe_allow_html=True
#         )
#     else:
#         start_time = time.time()

#         op = preprocess(paragraph.title())
#         sentences = [' '.join(sentence) for sentence in op]
        
#         tf_idf_scores = tf_idf(op)
        
#         sentence_scores = []
#         for idx, sentence_scores_dict in enumerate(tf_idf_scores):
#             sentence_total_score = sum(sentence_scores_dict.values())
#             sentence_scores.append((idx, sentence_total_score))
        
#         sentence_scores.sort(key=lambda x: x[1], reverse=True)
        
#         top_sentences_idx = [idx for idx, score in sentence_scores[:4]]
        
#         top_sentences_idx.sort()
        
#         summarized_text = " ".join([sentences[idx] for idx in top_sentences_idx])

#         summarized_text_2 = replace_synonyms(summarized_text)
#         end_time = time.time()
#         elapsed_time = end_time - start_time
        
#         st.subheader('Summarized Text:')
#         st.write(summarized_text_2)

#         st.markdown(
#             f'<p style="color: red; font-style: italic;">The execution time is: {elapsed_time:.4f} seconds</p>',
#             unsafe_allow_html=True
#         )

#     # example sentence 1
#     # कुत्रा (Canis familiaris किंवा Canis lupus familiaris) हा लांडग्याचा पाळीव वंशज आहे. याला पाळीव कुत्रा असेही म्हणतात, लेट प्लाइस्टोसीनच्या काळात लांडग्यांच्या नामशेष झालेल्या लोकसंख्येतून, 14,000 वर्षांपूर्वी, शेतीच्या विकासापूर्वी शिकारी-संकलकांनी पाळले होते. कुत्रा ही मानवाने पाळलेली पहिली प्रजाती होती. तज्ञांचा असा अंदाज आहे की मानवांशी त्यांच्या दीर्घ सहवासामुळे, कुत्र्यांनी मोठ्या संख्येने घरगुती व्यक्तींपर्यंत विस्तार केला आहे आणि स्टार्च-समृद्ध आहारावर भरभराट करण्याची क्षमता प्राप्त केली आहे जी इतर कॅनिड्ससाठी अपुरी असेल.[4]

#     # example sentence 2
#     # भारत, अधिकृतपणे भारतीय प्रजासत्ताक (ISO: Bharat Gaṇarājya),[21] दक्षिण आशियातील एक देश आहे. क्षेत्रफळानुसार हा सातव्या क्रमांकाचा देश आहे; जून 2023 पासून सर्वात जास्त लोकसंख्या असलेला देश;[22][23] आणि 1947 मध्ये स्वातंत्र्य मिळाल्यापासून, जगातील सर्वाधिक लोकसंख्या असलेला लोकशाही.[24][25][26] दक्षिणेला हिंद महासागर, नैऋत्येला अरबी समुद्र आणि आग्नेयेला बंगालच्या उपसागराने वेढलेले, ते पश्चिमेला पाकिस्तानशी जमीन सीमा सामायिक करते;[j] उत्तरेला चीन, नेपाळ आणि भूतान; आणि पूर्वेला बांगलादेश आणि म्यानमार. हिंदी महासागरात, भारत श्रीलंका आणि मालदीवच्या परिसरात आहे; त्याची अंदमान आणि निकोबार बेटे थायलंड, म्यानमार आणि इंडोनेशियाशी सागरी सीमा सामायिक करतात.

#? second iteration
# import streamlit as st
# import time
# from src.utils.preprocess import preprocess
# from src.tf_idf.td_idf import tf_idf
# from src.utils.replace_synonyms import replace_synonyms

# # UI code

# # set the title of the page
# st.set_page_config(
#     page_title='मराठी Text-Summarizer'
# )

# # set header for the page
# st.header('Welcome to the मराठी Text-Summarizer')

# # input elements
# st.subheader('')
# paragraph = st.text_area(
#     "Enter the text you want to summarize",
#     height=200
# )

# # button for submitting input
# submitButton = st.button(
#     label="Summarize"
# )

# # functionality on submit
# if(submitButton):
#     if(paragraph.strip() == ""):
#         st.markdown(
#             f'<p style="color: red; font-style: italic; font-weight:900;">No text provided</p>',
#             unsafe_allow_html=True
#         )
#     else:
#         start_time = time.time()

#         op = preprocess(paragraph.title())
#         sentences = [' '.join(sentence) for sentence in op]
        
#         tf_idf_scores = tf_idf(op)
        
#         sentence_scores = []
#         for idx, sentence_scores_dict in enumerate(tf_idf_scores):
#             sentence_total_score = sum(sentence_scores_dict.values())
#             sentence_scores.append((idx, sentence_total_score))
        
#         sentence_scores.sort(key=lambda x: x[1], reverse=True)
        
#         top_sentences_idx = [idx for idx, score in sentence_scores[:4]]
        
#         top_sentences_idx.sort()
        
#         # Add full stop to each selected sentence
#         summarized_text = " ".join([sentences[idx] + "." for idx in top_sentences_idx])

#         summarized_text_2 = replace_synonyms(summarized_text)
#         end_time = time.time()
#         elapsed_time = end_time - start_time
        
#         st.subheader('Summarized Text:')
#         st.write(summarized_text_2)

#         # Highlighting only selected sentences in yellow from the original text
#         highlighted_text = ""
#         for idx, sentence in enumerate(sentences):
#             if idx in top_sentences_idx:
#                 highlighted_text += f"<span style='background-color: white; color:red; font-style:italic; border:2px solid white;'>{sentence}.</span> "
#             else:
#                 highlighted_text += f"{sentence}. "

#         st.subheader('Highlighted sentences from original text:')

#         # Display the text with highlights
#         st.markdown(f"<p>{highlighted_text}</p>", unsafe_allow_html=True)

#         st.markdown(
#             f'<p style="color: red; font-style: italic;">The execution time is: {elapsed_time:.4f} seconds</p>',
#             unsafe_allow_html=True
#         )

#? 3rd iteration
# import streamlit as st
# import time
# from src.utils.preprocess import preprocess
# from src.tf_idf.td_idf import tf_idf
# from src.utils.replace_synonyms import replace_synonyms

# # UI code

# # set the title of the page
# st.set_page_config(
#     page_title='मराठी Text-Summarizer'
# )

# # set header for the page
# st.header('Welcome to the मराठी Text-Summarizer')

# # input elements
# st.subheader('')
# paragraph = st.text_area(
#     "Enter the text you want to summarize",
#     height=200
# )

# # button for submitting input
# submitButton = st.button(
#     label="Summarize"
# )

# # functionality on submit
# if(submitButton):
#     if(paragraph.strip() == ""):
#         st.markdown(
#             f'<p style="color: red; font-style: italic; font-weight:900;">No text provided</p>',
#             unsafe_allow_html=True
#         )
#     else:
#         start_time = time.time()

#         # Preprocess and tokenize the input text
#         op = preprocess(paragraph.title())
#         sentences = [' '.join(sentence) for sentence in op]
        
#         # Calculate TF-IDF scores
#         tf_idf_scores = tf_idf(op)
        
#         sentence_scores = []
#         for idx, sentence_scores_dict in enumerate(tf_idf_scores):
#             sentence_total_score = sum(sentence_scores_dict.values())
#             sentence_scores.append((idx, sentence_total_score))
        
#         sentence_scores.sort(key=lambda x: x[1], reverse=True)
        
#         top_sentences_idx = [idx for idx, score in sentence_scores[:4]]
        
#         top_sentences_idx.sort()
        
#         # Add full stop to each selected sentence
#         summarized_text = " ".join([sentences[idx] + "." for idx in top_sentences_idx])

#         # Replace synonyms in the summarized text and track replaced words
#         summarized_text_2, replaced_words = replace_synonyms(summarized_text)
#         end_time = time.time()
#         elapsed_time = end_time - start_time
        
#         # Display the summarized text with synonyms highlighted
#         st.subheader('Summarized Text:')
#         highlighted_summarized_text = summarized_text_2
#         for original, synonym in replaced_words.items():
#             highlighted_summarized_text = highlighted_summarized_text.replace(synonym, f"<span style='background-color: blue; color: white;'>{synonym}</span>")
#         st.markdown(f"<p>{highlighted_summarized_text}</p>", unsafe_allow_html=True)

#         # Highlighting only selected sentences in yellow and replaced words in blue in the original text
#         highlighted_text = ""
#         for idx, sentence in enumerate(sentences):
#             if idx in top_sentences_idx:
#                 # Highlight selected sentences in yellow
#                 highlighted_sentence = f"<span style='background-color: yellow; color:black; font-style:italic;'>{sentence}.</span> "
                
#                 # Further highlight any synonym-replaced words in blue
#                 for original, synonym in replaced_words.items():
#                     highlighted_sentence = highlighted_sentence.replace(synonym, f"<span style='background-color: blue; color: white;'>{synonym}</span>")
                
#                 highlighted_text += highlighted_sentence
#             else:
#                 # Regular sentence without any highlight
#                 highlighted_text += f"{sentence}. "

#         st.subheader('Highlighted sentences from original text:')

#         # Display the text with highlights
#         st.markdown(f"<p>{highlighted_text}</p>", unsafe_allow_html=True)

#         # Display execution time
#         st.markdown(
#             f'<p style="color: red; font-style: italic;">The execution time is: {elapsed_time:.4f} seconds</p>',
#             unsafe_allow_html=True
#         )

#? 4th iteration
# import streamlit as st
# import time
# from src.tf_idf.td_idf import summarize_text

# # UI code

# # set the title of the page
# st.set_page_config(
#     page_title='मराठी Text-Summarizer'
# )

# # set header for the page
# st.header('Welcome to the मराठी Text-Summarizer')

# # input elements
# st.subheader('')
# paragraph = st.text_area(
#     "Enter the text you want to summarize",
#     height=200
# )

# # button for submitting input
# submitButton = st.button(
#     label="Summarize"
# )

# # functionality on submit
# if submitButton:
#     if paragraph.strip() == "":
#         st.markdown(
#             f'<p style="color: red; font-style: italic; font-weight:900;">No text provided</p>',
#             unsafe_allow_html=True
#         )
#     else:
#         start_time = time.time()
        
#         # Call the summarization function in td_idf.py
#         highlighted_summarized_text, highlighted_original_text = summarize_text(paragraph)

#         end_time = time.time()
#         elapsed_time = end_time - start_time

#         # Display the summarized text with synonyms highlighted
#         st.subheader('Summarized Text:')
#         st.markdown(f"<p>{highlighted_summarized_text}</p>", unsafe_allow_html=True)

#         # Display the original text with highlighted sentences and synonym replacements
#         st.subheader('Highlighted sentences from original text:')
#         st.markdown(f"<p>{highlighted_original_text}</p>", unsafe_allow_html=True)



#         # Display execution time
#         st.markdown(
#             f'<p style="color: red; font-style: italic;">The execution time is: {elapsed_time:.4f} seconds</p>',
#             unsafe_allow_html=True
#         )

#? 5th iteration
import streamlit as st
import time
from src.tf_idf.td_idf import summarize_text
from src.lsa.lsa import summarize_text_lsa
from src.cosine.cosine import summarize_text_cosine
from src.textrank.textrank import summarize_text_textrank

# UI code

# set the title of the page
st.set_page_config(page_title='मराठी Text-Summarizer', layout="wide")

# set header for the page
st.header('Welcome to the मराठी Text-Summarizer')

# input elements
st.subheader('')
paragraph = st.text_area("Enter the text you want to summarize", height=200)

# button for submitting input
submitButton = st.button(label="Summarize")

# functionality on submit
if submitButton:
    if paragraph.strip() == "":
        st.markdown(
            f'<p style="color: red; font-style: italic; font-weight:900;">No text provided</p>',
            unsafe_allow_html=True
        )
    else:
        start_time = time.time()

        # Call all summarization functions
        tf_idf_summary, tf_idf_original = summarize_text(paragraph)
        lsa_summary, lsa_original = summarize_text_lsa(paragraph)
        cosine_summary, cosine_original = summarize_text_cosine(paragraph)
        textrank_summary, textrank_original = summarize_text_textrank(paragraph)

        end_time = time.time()
        elapsed_time = end_time - start_time

        # Create a 2x2 grid for displaying results
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        with col1:
            st.subheader("TF-IDF Summary")
            st.markdown(f"<p>{tf_idf_summary}</p>", unsafe_allow_html=True)
            with st.expander("Show original text with highlights"):
                st.markdown(f"<p>{tf_idf_original}</p>", unsafe_allow_html=True)

        with col2:
            st.subheader("LSA Summary")
            st.markdown(f"<p>{lsa_summary}</p>", unsafe_allow_html=True)
            with st.expander("Show original text with highlights"):
                st.markdown(f"<p>{lsa_original}</p>", unsafe_allow_html=True)

        with col3:
            st.subheader("Cosine Similarity Summary")
            st.markdown(f"<p>{cosine_summary}</p>", unsafe_allow_html=True)
            with st.expander("Show original text with highlights"):
                st.markdown(f"<p>{cosine_original}</p>", unsafe_allow_html=True)

        with col4:
            st.subheader("TextRank Summary")
            st.markdown(f"<p>{textrank_summary}</p>", unsafe_allow_html=True)
            with st.expander("Show original text with highlights"):
                st.markdown(f"<p>{textrank_original}</p>", unsafe_allow_html=True)

        # Display execution time
        st.markdown(
            f'<p style="color: red; font-style: italic;">The execution time is: {elapsed_time:.4f} seconds</p>',
            unsafe_allow_html=True
        )