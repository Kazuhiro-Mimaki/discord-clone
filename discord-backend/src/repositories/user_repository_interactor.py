from .user_repository_interface import IUserRepository


class UserRepository(IUserRepository):
    def get_by_email(self, email: str):
        pass

    def create(self, name: str, email: str, password: str):
        pass
