import weaviate
import json

client = weaviate.Client(
    url="https://article-recommender.weaviate.network/",  # Replace with your endpoint
    additional_headers={
        "X-Cohere-Api-Key": "8bwgk1enPcRPjW7TlmsAwgyjKWPZJyRZNSUDFbWb"  # Replace with your API key
    }
)

client.schema.delete_all()
schema = {
    "classes": [
        {
            "class": "Article",
            "vectorizer": "text2vec-cohere",
            "properties": [
                {
                    "name": "category",
                    "dataType": ["text"],
                    "description": "article category"
                },
                {
                    "name": "heading",
                    "dataType": ["text"],
                    "description": "article title"
                },
                {
                    "name": "article",
                    "dataType": ["text"],
                    "description": "article content"
                }
            ]
        }
    ]
}

# create the schema
client.schema.create(schema)

# get the schema
schema = client.schema.get()

# print the schema
print(json.dumps(schema, indent=4))
