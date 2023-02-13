import streamlit as st
import time
from search import near_text_search

st.set_page_config(
    page_title="Random Search Results",
    page_icon="🔫",
)

st.markdown("# Near Text Search Results")
st.sidebar.header("Get Near Text")
st.write(
    """
        We are going to get the nearest search results based on article genre, distance, and certain criteria
    """
)

# Get input parameters from the user to perform the search
concepts = st.multiselect(
    'Select the article topics to search: ',
    ['business', 'entertainment', 'politics', 'sport', 'tech'],
)
dist = st.number_input('Enter the distance: ', min_value=0.0, max_value=1.0, step=0.1)
choice = st.radio('Choose any one of the them: ', ('distance', 'certainty'))

with st.spinner('Searching...'):
    if st.button('Search🔍'):
        time.sleep(4)
        st.json(near_text_search(concepts, dist, choice))

st.button("Go to home", disabled=True)
st.button("Try next Search", disabled=True)
