import weaviate
import os
from dotenv import load_dotenv
load_dotenv()

Client = weaviate.Client(
    url=os.environ.get("WEAVIATE_URL"),  # Replace with your endpoint
    additional_headers={
        "X-Cohere-Api-Key":os.environ.get("COHERE_API_KEY")  # Replace with your API key
    })
