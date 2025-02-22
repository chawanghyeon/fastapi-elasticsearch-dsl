from repositories.base_repository import BaseRepository

class CRUDService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def get(self, id: str):
        return self.repository.get(id)

    def create(self, data: dict):
        return self.repository.create(data)

    def update(self, id: str, data: dict):
        return self.repository.update(id, data)

    def delete(self, id: str):
        return self.repository.delete(id)
