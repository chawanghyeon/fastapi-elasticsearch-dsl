from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def get(self, id: str):
        pass

    @abstractmethod
    def create(self, data: dict):
        pass

    @abstractmethod
    def update(self, id: str, data: dict):
        pass

    @abstractmethod
    def delete(self, id: str):
        pass
