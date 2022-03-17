from pydantic import BaseModel


class UserSignupRequest(BaseModel):
    name: str
    email: str
    password: str
