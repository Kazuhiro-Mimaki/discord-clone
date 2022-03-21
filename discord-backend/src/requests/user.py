from pydantic import BaseModel


class UserSignupRequest(BaseModel):
    name: str
    email: str
    password: str


class UserSigninRequest(BaseModel):
    email: str
    password: str
