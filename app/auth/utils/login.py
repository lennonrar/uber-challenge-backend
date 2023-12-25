from datetime import timedelta
from app.auth.config import settings


def get_access_token_expires():
    return timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
