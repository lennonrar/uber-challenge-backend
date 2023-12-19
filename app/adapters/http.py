from fastapi import FastAPI, HTTPException, status
from app.core.use_cases.create_update_user import (create_user_use_case,
                                                   update_user_use_case)


app = FastAPI()


@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user_route(username: str, email: str):
    """
    Create a user route.

    Args:
        username (str): The username of the user.
        email (str): The email of the user.

    Returns:
        dict: A dictionary containing the user information.

    Raises:
        HTTPException: If an error occurs while creating the user.
    """
    try:
        user = create_user_use_case(username, email)
        return {"user": user}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e))


@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user_route(user_id: int, user_data: dict):
    """
    Update a user route.

    Args:
        user_id (int): The ID of the user to update.
        user_data (dict): A dictionary with the data to update.

    Returns:
        dict: A dictionary containing the updated user information.

    Raises:
        HTTPException: If an error occurs while updating the user.
    """
    try:
        user = update_user_use_case(user_id, user_data)
        return {"user": user}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=str(e))
