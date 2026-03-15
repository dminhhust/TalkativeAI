from jose import jwt
from datetime import datetime, timedelta
from app.config import *

def create_token(user_id: int):

    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)

    payload = {
        "user_id": user_id,
        "exp": expire
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token


def verify_token(token: str):

    payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

    return payload["user_id"]
