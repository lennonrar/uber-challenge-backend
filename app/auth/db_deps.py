from app.auth.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import Generator, Type, Annotated


def get_db() -> Generator[Type[Session], None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependencies = Annotated[Session, Depends(get_db)]
