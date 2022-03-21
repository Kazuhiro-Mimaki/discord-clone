from ..requests import UserSignupRequest, UserSigninRequest
from src.repositories import IUserRepository, UserRepository
import hashlib, os, jwt


class UserUseCase:
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def signup(self, req: UserSignupRequest):
        try:
            # check if user exists
            exist_user = self.user_repository.get_by_email(email=req.email)
            if exist_user:
                return "email already in use.", 409

            # encrypt password
            encryptedPassword = hashlib.sha256((req.password + '10').encode()).hexdigest()

            # create user document and save in database
            user_id = self.user_repository.create(name=req.name, email=req.email, password=encryptedPassword)

            # create JWT token
            token = jwt.encode({"user_id": user_id}, os.getenv('TOKEN_KEY'), algorithm="HS256")

            return  {
                "email": req.email,
                "name": req.name,
                "token": token
            }, 200
        except Exception as e:
            print(e)
            return "error occured. please try again", 500

    def signin(self, req: UserSigninRequest):
        try:
            # check if user exist
            user = self.user_repository.get_by_email(email=req.email)

            # encrypt password
            encryptedPassword = hashlib.sha256((req.password + '10').encode()).hexdigest()

            # check valid
            if not user or user.password != encryptedPassword:
                return "invalid credentials. Please try again", 400
            
            # create JWT token
            token = jwt.encode({"user_id": user.id}, os.getenv('TOKEN_KEY'), algorithm="HS256")

            return  {
                "email": user.email,
                "name": user.name,
                "token": token
            }, 200
            
        except Exception as e:
            print(e)
            return "something went wrong. Please try again", 500


user_usecase = UserUseCase(user_repository=UserRepository())
