import pandas as pd
from client import Client

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

Client.batch.configure(
  batch_size=10, 
  # dynamically update the `batch_size` based on import speed
  dynamic=True,
  timeout_retries=3,
)

data=pd.read_csv('headings.csv')

for i in range (0,len(data)):
    item = data.iloc[i]

    article_object = {
        'article': str(item['Article']),
        'category':str(item['Category']),
        'heading':str(item['Heading'])
    }

    try:
        Client.batch.add_data_object(article_object, 'Article')
    except BaseException as error:
        print("Import Failed at: ",i)
        print("An exception occurred: {}".format(error))
        # Stop the import on error
        break

    print("Status: ", str(i)+"/"+str(len(data)-1))

Client.batch.flush()
print('Job done...')
