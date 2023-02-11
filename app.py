import streamlit as st

st.title('Weaviate Artcile Vector Search Engine')
st.header('Made use of Weaviate + Streamlit for searching the articles data gathered from Kaggle')

with st.sidebar:
    add_radio = st.radio(
        "Choose searching method",
        ("Get `n` random objects", "Using near-text search",
         "Using vector search", "Using bm25", "Using metadata with aggregate"),
    )


