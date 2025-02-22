
from elasticsearch import Elasticsearch

class ElasticSearchClient:
    def __init__(self, es_url: str):
        self.client = Elasticsearch(es_url)

    def create_index(self, index_name: str, body: dict):
        self.client.indices.create(index=index_name, body=body)

    def delete_index(self, index_name: str):
        self.client.indices.delete(index=index_name)
