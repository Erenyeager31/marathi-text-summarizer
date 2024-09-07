# import the required modules
import streamlit as st
import time
from src.utils.preprocess import preprocess
from src.tf_idf.td_idf import tf_idf
from src.utils.replace_synonyms import replace_synonyms

# UI code

# set the title of the page
st.set_page_config(
    page_title='मराठी Text-Summarizer'
)

# set header for the page
st.header('Welcome to the मराठी Text-Summarizer')

# input elements
st.subheader('')
paragraph = st.text_area(
    "Enter the text you want to summarize",
    height=200
)

# button for submitting input
submitButton = st.button(
    label="Summarize"
)

# functionality on submit
if(submitButton):
    if(paragraph.title() == ""):
        st.markdown(
            f'<p style="color: red; font-style: italic; font-weight:900;">No text provided</p>',
            unsafe_allow_html=True
        )
    else:
        start_time = time.time()

        op = preprocess(paragraph.title())
        sentences = [' '.join(sentence) for sentence in op]
        
        tf_idf_scores = tf_idf(op)
        
        sentence_scores = []
        for idx, sentence_scores_dict in enumerate(tf_idf_scores):
            sentence_total_score = sum(sentence_scores_dict.values())
            sentence_scores.append((idx, sentence_total_score))
        
        sentence_scores.sort(key=lambda x: x[1], reverse=True)
        
        top_sentences_idx = [idx for idx, score in sentence_scores[:2]]
        
        top_sentences_idx.sort()
        
        summarized_text = " ".join([sentences[idx] for idx in top_sentences_idx])

        summarized_text_2 = replace_synonyms(summarized_text)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        st.subheader('Summarized Text:')
        st.write(summarized_text_2)

        st.markdown(
            f'<p style="color: red; font-style: italic;">The execution time is: {elapsed_time:.4f} seconds</p>',
            unsafe_allow_html=True
        )

    # example sentence 1
    # कुत्रा (Canis familiaris किंवा Canis lupus familiaris) हा लांडग्याचा पाळीव वंशज आहे. याला पाळीव कुत्रा असेही म्हणतात, लेट प्लाइस्टोसीनच्या काळात लांडग्यांच्या नामशेष झालेल्या लोकसंख्येतून, 14,000 वर्षांपूर्वी, शेतीच्या विकासापूर्वी शिकारी-संकलकांनी पाळले होते. कुत्रा ही मानवाने पाळलेली पहिली प्रजाती होती. तज्ञांचा असा अंदाज आहे की मानवांशी त्यांच्या दीर्घ सहवासामुळे, कुत्र्यांनी मोठ्या संख्येने घरगुती व्यक्तींपर्यंत विस्तार केला आहे आणि स्टार्च-समृद्ध आहारावर भरभराट करण्याची क्षमता प्राप्त केली आहे जी इतर कॅनिड्ससाठी अपुरी असेल.[4]

    # example sentence 2
    # भारत, अधिकृतपणे भारतीय प्रजासत्ताक (ISO: Bharat Gaṇarājya),[21] दक्षिण आशियातील एक देश आहे. क्षेत्रफळानुसार हा सातव्या क्रमांकाचा देश आहे; जून 2023 पासून सर्वात जास्त लोकसंख्या असलेला देश;[22][23] आणि 1947 मध्ये स्वातंत्र्य मिळाल्यापासून, जगातील सर्वाधिक लोकसंख्या असलेला लोकशाही.[24][25][26] दक्षिणेला हिंद महासागर, नैऋत्येला अरबी समुद्र आणि आग्नेयेला बंगालच्या उपसागराने वेढलेले, ते पश्चिमेला पाकिस्तानशी जमीन सीमा सामायिक करते;[j] उत्तरेला चीन, नेपाळ आणि भूतान; आणि पूर्वेला बांगलादेश आणि म्यानमार. हिंदी महासागरात, भारत श्रीलंका आणि मालदीवच्या परिसरात आहे; त्याची अंदमान आणि निकोबार बेटे थायलंड, म्यानमार आणि इंडोनेशियाशी सागरी सीमा सामायिक करतात.