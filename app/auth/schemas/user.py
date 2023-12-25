from pydantic import BaseModel
from typing import Annotated


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool = True
    is_admin: bool = False
    description: str | None

    class Config:
        orm_mode = True
