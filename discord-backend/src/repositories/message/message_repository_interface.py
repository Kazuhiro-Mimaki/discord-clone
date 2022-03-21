from abc import ABC, abstractmethod

class IMessageRepository(ABC):
    @abstractmethod
    def get_list(self):
        raise NotImplementedError()

    @abstractmethod
    def create(self, content: str):
        raise NotImplementedError()
