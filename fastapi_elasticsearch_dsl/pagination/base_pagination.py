from abc import ABC, abstractmethod

class BasePagination(ABC):
    @abstractmethod
    def paginate(self, query, page, size):
        pass
