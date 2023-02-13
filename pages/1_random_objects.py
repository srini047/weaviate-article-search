import streamlit as st
import time
from search import random_objects

st.set_page_config(
    page_title="Random Search Results",
    page_icon="🔢",
)

st.markdown("# Random Object")
st.sidebar.header("Get Random Object(s)")
st.write(
    """
        We are going to get `n` random objects from the dataset as per number selected by the user.
    """
)

n = st.slider('Select the number of random objects to be generated:', 0, 25, value=5, step=1)

with st.spinner('Searching...'):
    if st.button('Search🔍'):
        time.sleep(4)
        st.write(random_objects(n))

st.button("Go to home", disabled=True)
st.button("Try next Search", disabled=True)
