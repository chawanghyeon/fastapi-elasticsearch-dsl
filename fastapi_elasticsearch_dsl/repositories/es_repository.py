from .base_repository import BaseRepository
from elasticsearch import Elasticsearch

class ESRepository(BaseRepository):
    def __init__(self, es_client: Elasticsearch):
        self.es_client = es_client

    def get(self, id: str):
        return self.es_client.get(index="my_index", id=id)

    def create(self, data: dict):
        return self.es_client.index(index="my_index", body=data)

    def update(self, id: str, data: dict):
        return self.es_client.update(index="my_index", id=id, body={"doc": data})

    def delete(self, id: str):
        return self.es_client.delete(index="my_index", id=id)
