from typing import Dict

from app.auth.models.user import UserBase

from app.auth.schemas.user import Users
from sqlmodel import select


def get_users_use_case(session, skip: int = 0, limit: int = 10):
    """
    Retrieve users.
    """
    statement = select(Users).offset(skip).limit(limit)
    users = session.exec(statement).all()
    return users


def create_user_use_case(username: str, email: str) -> UserBase:
    """
    Create a new user.

    Args:
        username (str): The username for the new user.
        email (str): The email for the new user.

    Returns:
        UserModel: The created user.
    """

    if not username or email:
        raise ValueError("Username and email are required")

    user_data: Dict[str, str] = {
        'username': username,
        'email': email
    }

    return create_update_user(user_data) # TODO call core


def update_user_use_case(user_id: int,
                         update_data: Dict[str, str]) -> UserBase:
    """
    Update an existing user.

    Args:
        user_id (int): The ID of the user to update.
        update_data (Dict[str, str]): A dictionary with the data to update.

    Returns:
        UserModel: The updated user.
    """

    if not user_id or not update_data:
        raise ValueError("User ID and update data are required")

    update_data['id'] = user_id
 
    return create_update_user(update_data) # TODO call core
