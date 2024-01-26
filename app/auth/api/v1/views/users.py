from fastapi import (HTTPException,
                     status,
                     APIRouter,
                     Depends)
from typing import Annotated
from sqlalchemy.orm import Session

from app.auth import crud, schemas
from app.auth.db_deps import get_db
from app.auth.utils.oauth2 import oauth2_scheme
from app.auth.api.v1.dependencies import get_current_user

router = APIRouter()


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate,
                db: Session = Depends(get_db)
                ):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=list[schemas.User])
def read_users(
    token: Annotated[str, Depends(oauth2_scheme)],
    skip: int = 0, limit: int = 100,
    db: Session = Depends(get_db)
):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    return db_user


@router.get("/me/", response_model=schemas.User)
async def read_users_me(
        current_user: Annotated[schemas.User, Depends(get_current_user)]):
    return current_user
