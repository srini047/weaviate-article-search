import streamlit as st
import time
from search import bm_25

st.set_page_config(
    page_title="bm25",
    page_icon="🔢",
)

st.markdown("# BM25")
st.sidebar.header("Get object(s) ranked by bm25")
st.write("""
        We are going to search objects from the dataset using BM25 ranking system
    """)

query = st.text_input('Enter the query to be searched: ',
                      value='vector search engine',
                      max_chars=50)
query = {"query": query}

with st.spinner('Searching...'):
    if st.button('Search🔍'):
        time.sleep(4)
        st.write(bm_25(query))

st.button("Go to home", disabled=True)
st.button("Try next Search", disabled=True)
