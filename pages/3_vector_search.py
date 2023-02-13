import streamlit as st
import time
from search import vector_search

st.set_page_config(
    page_title="Vector search",
    page_icon="🔫",
)

st.markdown("# Vector Search")
st.sidebar.header("Searching using Vector Search")
st.write(
    """
        We are going to perform a generic search, and use some additional parameters
    """
)

st.warning('Under development', icon="🏗️")
st.snow()

# about = st.text_input('Enter the search term: ', value='vector search engine', max_chars=50)
# alpha = st.number_input('Set the alpha value: ', min_value=0.0, max_value=1.0, step=0.1)

# with st.spinner('Searching...'):
#     if st.button('Search🔍'):
#         time.sleep(4)
#         st.write(vector_search(about, alpha))

st.button("Go to home", disabled=True)
st.button("Try next Search", disabled=True)
