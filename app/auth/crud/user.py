from sqlalchemy.orm import Session
from app.auth import models, schemas
from app.auth.core import token


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    user.password = token.get_password_hash(user.password)
    db_user = models.Users(name=user.name, 
                           email=user.email, 
                           password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
