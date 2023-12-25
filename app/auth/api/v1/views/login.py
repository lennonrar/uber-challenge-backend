from fastapi import (
    HTTPException,
    status,
    APIRouter,
    Depends)
from typing import Annotated
from app.auth import schemas

from fastapi.security import OAuth2PasswordRequestForm
from app.auth.core import authenticate_user, create_access_token
from app.auth.db_deps import get_db
from sqlalchemy.orm import Session
from app.auth.utils.login import get_access_token_expires

router = APIRouter()


@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user(db,
                             form_data.username,
                             form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=get_access_token_expires()
    )
    return {"access_token": access_token, "token_type": "bearer"}
