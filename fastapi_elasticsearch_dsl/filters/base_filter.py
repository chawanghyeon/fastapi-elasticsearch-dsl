from abc import ABC, abstractmethod

class BaseFilter(ABC):
    @abstractmethod
    def apply(self, query: dict, value: str):
        pass
