from app.core.modules.user import User as UserModel


class User:
    def __init__(self, data: UserModel):
        self.name = data.name
        self.description = data.description
        self.email = data.email
        self.password: str = data.password
        self.is_active: bool = True
        self.is_admin: bool = False
        self.is_superuser: bool = False


def set_password(user: UserModel, password: str) -> str:
    user.password = password
    return password


def check_password(password: str) -> bool:
    # TODO: Implement password check
    return True


def actvivate(user: UserModel) -> User:
    user.is_active = True
    return user


def deactivate(user: UserModel) -> User:
    user.is_active = False
    return user


def create_update_user(data: UserModel) -> User:
    if 'id' in data:
        data.pop('id')

    user = User(**data)

    # Additional enhancements
    user.is_active = True
    user.is_admin = False
    user.is_superuser = False

    # Set a default password if not provided
    if not user.password:
        user.password = user.set_password(generate_default_password())

    return user


def generate_default_password() -> str:
    # TODO: Implement password generation logic
    return "default_password"
