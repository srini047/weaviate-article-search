import json
from client import Client

Client.schema.delete_all()
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
Client.schema.create(schema)

# get the schema
schema = Client.schema.get()

# print the schema
print(json.dumps(schema, indent=4))
