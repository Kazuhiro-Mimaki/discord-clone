from src.models.user import UserModel
from .user_repository_interface import IUserRepository
from src.repositories.db import USER, session


class UserRepository(IUserRepository):
    def get_by_email(self, email: str) -> UserModel:
        return session.query(USER).filter(USER.email == email).first()

    def create(self, name: str, email: str, password: str) -> int:
        db_user = USER(name=name, email=email, password=password)
        session.add(db_user)
        session.commit()
        return db_user.id
