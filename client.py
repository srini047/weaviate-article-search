import weaviate
import json

Client = weaviate.Client(
    url=
    "https://article-recommender.weaviate.network/",  # Replace with your endpoint
    additional_headers={
        "X-Cohere-Api-Key":
        "8bwgk1enPcRPjW7TlmsAwgyjKWPZJyRZNSUDFbWb"  # Replace with your API key
    })
