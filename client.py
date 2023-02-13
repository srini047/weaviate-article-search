import weaviate
# import os
# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st

Client = weaviate.Client(
    # url=os.environ.get("WEAVIATE_URL"),  # Replace with your endpoint
    url=st.secrets["WEAVIATE_URL"],
    additional_headers={
        # "X-Cohere-Api-Key":os.environ.get("COHERE_API_KEY")  # Replace with your API key
        "X-Cohere-Api-Key":st.secrets["COHERE_API_KEY"]
    })
