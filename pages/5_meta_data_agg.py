import streamlit as st
import time
from search import meta_data_agg

st.set_page_config(
    page_title="bm25",
    page_icon="🔢",
)

st.markdown("# Metadata with Aggregate Results")
st.sidebar.header("Metadata search results")
st.write("""
        We are going to search objects from the dataset using metadata search and aggregate the results obtained as the corresponding count
    """)

about = st.selectbox('Enter the query to be searched: ', options=['business', 'entertainment', 'politics', 'sport', 'tech'])

with st.spinner('Searching...'):
    if st.button('Search🔍'):
        time.sleep(4)
        st.write(meta_data_agg(about))

st.button("Go to home", disabled=True)
st.button("Try next Search", disabled=True)
