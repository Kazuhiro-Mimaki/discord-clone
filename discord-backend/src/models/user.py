from dataclasses import dataclass


@dataclass(frozen=True)
class UserModel():
    name: str
    email: str
    password: str
