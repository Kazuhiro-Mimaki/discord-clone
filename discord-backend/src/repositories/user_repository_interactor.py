from .user_repository_interface import IUserRepository
from src.repositories.db import Base, engine, SessionLocal
from src.models import UserModel
from sqlalchemy.orm import Session


class UserRepository(IUserRepository):
    def get_by_email(self, email: str, db_session: Session):
        res = db_session.query(UserModel).filter(UserModel.email == email)
        print(res)
        return res

    def create(self, name: str, email: str, password: str):
        pass
