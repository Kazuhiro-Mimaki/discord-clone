from abc import ABC, abstractmethod

class IUserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str):
        raise NotImplementedError()

    @abstractmethod
    def create(self, name: str, email: str, password: str):
        raise NotImplementedError()
