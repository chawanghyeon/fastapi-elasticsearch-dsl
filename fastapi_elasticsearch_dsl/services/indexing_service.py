from repositories.es_repository import ESRepository

class IndexingService:
    def __init__(self, es_repository: ESRepository):
        self.es_repository = es_repository

    def index_document(self, data: dict):
        return self.es_repository.create(data)
