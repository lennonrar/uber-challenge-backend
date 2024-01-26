from typing import Annotated
from fastapi import Depends, HTTPException, status

from app.auth.schemas import User, TokenData
from app.auth.utils.oauth2 import oauth2_scheme
from jose import JWTError, jwt

from app.auth.config import settings
from app.auth.db_deps import get_db
from app.auth import crud
from sqlalchemy.orm import Session

SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Annotated[str, Depends(oauth2_scheme)]


async def get_current_user(session: SessionDep, token: TokenDep):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(email=username)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_email(session, email=token_data.email)
    if user is None:
        raise credentials_exception

    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user
