from enum import Enum
from pydantic import BaseModel


class UserModel(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class UserModelPost(BaseModel):
    name: str
    description: str | None = None
    email: str
    password: str
    is_active: bool = True
    is_admin: bool = False
    is_superuser: bool = False


class UserModelPut(UserModelPost):
    user_id: int
