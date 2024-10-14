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

        paragraph1 = [sentence.strip() for sentence in paragraph.split('.') if sentence.strip()]
        n = len(paragraph1)

        # Determine the number of sentences to summarize (n/3)
        num_sentences = max(1, n // 3)  # At least one sentence

        # Call all summarization functions
        tf_idf_summary, tf_idf_original = summarize_text(paragraph,num_sentences)
        lsa_summary, lsa_original = summarize_text_lsa(paragraph,num_sentences)
        cosine_summary, cosine_original = summarize_text_cosine(paragraph,num_sentences)
        textrank_summary, textrank_original = summarize_text_textrank(paragraph,num_sentences)

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
