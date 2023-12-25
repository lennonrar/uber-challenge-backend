from fastapi import APIRouter

from app.auth.api.v1.views import login, users

api_router = APIRouter()
# api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
