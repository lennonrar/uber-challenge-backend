from enum import Enum
from pydantic import BaseModel


class UserModelEnum(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class UserModel(BaseModel):
    name: str
    description: str | None = None
    email: str
    password: str
    is_active: bool = True
    is_admin: bool = False
    is_superuser: bool = False


class UserModelUpdate(UserModel):
    user_id: int
