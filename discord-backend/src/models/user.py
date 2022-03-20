from dataclasses import dataclass
from pydantic import BaseModel


@dataclass(frozen=True)
class UserModel(BaseModel):
    name: str
    email: str
    password: str
