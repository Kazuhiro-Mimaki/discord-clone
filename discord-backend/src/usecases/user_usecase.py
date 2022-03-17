from ..requests import UserSignupRequest
from src.repositories import IUserRepository
import hashlib
import jwt
import os


class UserUseCase:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def signup(self, req: UserSignupRequest):
        # check if user exists
        exist_user = self.user_repository.get_by_email(email=req.email)
        if exist_user:
            return "email already in use.", 409

        # encrypt password
        encryptedPassword = hashlib.sha256(req.password+10)

        # create user document and save in database
        user = self.user_repository.create(name=req.name, email=req.email, password=encryptedPassword)

        # create JWT token
        token = jwt.encode({"user_id": user.id}, os.getenv('TOKEN_KEY'), algorithm="HS256")

        return {"user": {
            "email": user.email,
            "username": user.name,
            "token": token
        }}, 200

    def signin(self):
        return {"signin": "signin"}


user_usecase = UserUseCase()
