import pandas as pd
import helper
import weaviate

# initiate the Weaviate client
client = weaviate.Client("https://article-recommender.weaviate.network")
client.timeout_config = (3, 200)

# empty schema and create new schema
client.schema.delete_all()
schema = {
    "classes": [
        {
            "class": "Article",
            "properties": [
                {
                    "name": "description",
                    "dataType": ["text"]
                },
                {
                    "name": "title",
                    "dataType": ["text"]
                }
            ]
        }
    ]
}
client.schema.create(schema)

# open wine dataset (10000 items)
df = pd.read_csv('./articles.csv', index_col=0)

def add_articles(data, batch_size=512, debug_mode=False):
    """ upload articles to Weaviate

    :param data: article data in panda dataframe object
    :type data: panda dataframe object (2 columns: 'title' and 'description')
    :param batch_size: number of data objects to put in one batch, defaults to 512
    :type batch_size: int, optional
    :param debug_mode: set to True if you want to display upload errors, defaults to False
    :type debug_mode: bool, optional
    """    

    no_items_in_batch = 0

    for index, row in data.iterrows():
        article_object = {
            "title": row["title"] + '.',
            "description": row["article"],
        }

        article_uuid = helper.generate_uuid('article', row["title"]+row["article"])

        client.batch.add_data_object(article_object, "Wine", article_uuid)
        no_items_in_batch += 1

        if no_items_in_batch >= batch_size:
            results = client.batch.create_objects()
            
            if debug_mode:
                for result in results:
                    if result['result'] != {}:
                        helper.log(result['result'])

                message = str(index) + ' / ' + str(data.shape[0]) +  ' items imported'
                helper.log(message)

            no_items_in_batch = 0

    client.batch.create_objects()

add_articles(df.head(2500), batch_size=99, debug_mode=True)
