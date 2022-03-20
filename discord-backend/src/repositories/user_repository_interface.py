from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

class IUserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str, db_session: Session):
        raise NotImplementedError()

    @abstractmethod
    def create(self, name: str, email: str, password: str):
        raise NotImplementedError()
