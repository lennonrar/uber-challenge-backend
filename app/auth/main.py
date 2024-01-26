from fastapi import FastAPI
from app.auth.api.v1.api import api_router
from starlette.middleware.cors import CORSMiddleware

from fastapi import (FastAPI, 
                     HTTPException, 
                     status, 
                     APIRouter, 
                     Depends)
from sqlalchemy.orm import Session
from app.auth import crud, schemas
from app.auth.db_deps import get_db


BACKEND_CORS_ORIGINS = ["http://localhost", "http://localhost:4200", 
                        "http://localhost:3000", "http://localhost:8080",
                        "http://127.0.0.1:8000",
                        "http://local.dockertoolbox.tiangolo.com"]
app = FastAPI(
    title='FastAPI Auth Service',
    openapi_url="/api/v1/views/openapi.json",
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix='/api/v1')

# @app.post("/users", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
