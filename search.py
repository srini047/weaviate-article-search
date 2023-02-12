import weaviate
import json

client = weaviate.Client(
    url=
    "https://article-recommender.weaviate.network/",  # Replace with your endpoint
    additional_headers={
        "X-Cohere-Api-Key":
        "8bwgk1enPcRPjW7TlmsAwgyjKWPZJyRZNSUDFbWb"  # Replace with your API key
    })

# Returns 'n' random objects
# result = client.query.get("Article", ["heading", "category"]).with_limit(5).do()

# Using near text search - works fine
nearText = {
  "concepts": ["fashion"],
  "distance": 0.6, # prior to v1.14 use "certainty" instead of "distance"
  "moveAwayFrom": {
    "concepts": ["finance"],
    "force": 0.45
  },
  "moveTo": {
    "concepts": ["sport"],
    "force": 0.85
  }
}

result = (
    client.query
    .get("Article", ["category", "heading"])
    .with_additional(["distance"])
    .with_near_text(nearText)
    .do()
)

# Using vector search - works fine
# result = (
#   client.query
#   .get("Article", ["heading", "category"])
#   .with_hybrid("vector search engiene", alpha=0.5, vector=[1, 2, 3])
#   .do()
# )

# Using bm25 - works fine
# bm25 = {
#     "query" : "ChatGPT"
# }

# result = (
#   client.query
#   .get("Article", ["category", "heading", "_additional {score} "])
#   .with_bm25(bm25)
#   .do()
# )

# Using metadata with aggregate - works fine
# where_filter = {
#   "path": ["category"],
#   "operator": "Equal",
#   "valueString": "tech",   # Use either business, entertainment, politics, sport or tech 
# }

# result = (
#     client.query
#     .aggregate("Article")
#     .with_fields("meta {count}")
#     .with_where(where_filter)
#     .do()
# )

print(json.dumps(result, indent=2))
