from abc import ABC, abstractmethod

class BaseSerializer(ABC):
    @abstractmethod
    def serialize(self, obj):
        pass
