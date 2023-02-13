import time
import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

with st.spinner('Loading App 🌀'):
    time.sleep(1)

st.balloons()

st.title('Weaviate Article Vector Search Engine')
st.header('Made use of Weaviate + Streamlit for searching the articles data gathered from Kaggle')

st.sidebar.success("Select any of the above search...")


