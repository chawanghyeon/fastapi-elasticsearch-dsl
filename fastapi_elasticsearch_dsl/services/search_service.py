from repositories.es_repository import ESRepository

class SearchService:
    def __init__(self, es_repository: ESRepository):
        self.es_repository = es_repository

    def search(self, query: dict):
        return self.es_repository.es_client.search(index="my_index", body=query)
