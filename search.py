# import weaviate
# import json

# client = weaviate.Client(
#     url=
#     "https://article-recommender.weaviate.network/",  # Replace with your endpoint
#     additional_headers={
#         "X-Cohere-Api-Key":
#         "8bwgk1enPcRPjW7TlmsAwgyjKWPZJyRZNSUDFbWb"  # Replace with your API key
#     })

from client import Client

# Returns 'n' random objects
def random_objects(n: int) -> dict:
    # result = Client.query.get("Article", ["heading", "category", "article"]).with_limit(5).do()
    result = Client.query.get("Article", ["heading", "category", "article"]).with_limit(n).do()
    
    return result


# Using near text search - works fine
def near_text_search(
        # nearText = {
        #     "concepts": ["fashion"],
        #     "distance": 0.6,  # prior to v1.14 use "certainty" instead of "distance"
        #     "moveAwayFrom": {
        #         "concepts": ["finance"],
        #         "force": 0.45
        #     },
        #     "moveTo": {
        #         "concepts": ["sport"],
        #         "force": 0.85
        #     }
        # }
        concepts: list,
        dist: float,
        choice: str) -> dict:  # choice = "certainty" OR "distance"
    nearText = {
        "concepts": concepts,
        "distance":
        dist,  # prior to v1.14 use "certainty" instead of "distance"
        "moveAwayFrom": {
            "concepts": ["finance"],
            "force": 0.45
        },
        "moveTo": {
            "concepts": ["sport"],
            "force": 0.85
        }
    }
    result = (Client.query.get(
        "Article", ["category", "heading", "article"
                    ]).with_additional(choice).with_near_text(nearText).do())

    return result


# Using vector search - works fine
def vector_search(about: str, alpha: float) -> dict:
    result = (Client.query.get("Article",
                               ["heading", "category", "article"]).with_hybrid(
                                   about, alpha=alpha, vector=[1, 2, 3]).do())
    print(alpha)

    return result


# Using bm25 - works fine
def bm_25(bm25: dict) -> dict:
    # bm25 = {
    #     "query" : "ChatGPT"
    # }
    result = (Client.query.get(
        "Article", ["category", "heading", "article", "_additional {score} "
                    ]).with_bm25(bm25).do())

    return result


# Using metadata with aggregate - works fine
def meta_data_agg(about: str) -> dict:
    # where_filter = {
    #   "path": ["category"],
    #   "operator": "Equal",
    #   "valueString": "",   # Use either business, entertainment, politics, sport or tech
    # }
    where_filter = {
        "path": ["category"],
        "operator": "Equal",
        "valueString":
        about,  # Use either business, entertainment, politics, sport or tech
    }

    result = (Client.query.aggregate("Article").with_fields(
        "meta {count}").with_where(where_filter).do())

    return result


# print(json.dumps(result, indent=2))
# print(meta_data_agg())
# print(bm_25({"query" : "ChatGPT"}))
