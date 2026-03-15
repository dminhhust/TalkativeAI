from fastapi import Request, HTTPException
from jose import jwt
from app.config import *


async def verify_auth(request: Request):

    auth_header = request.headers.get("Authorization")

    if auth_header is None:
        raise HTTPException(status_code=401, detail="Missing token")

    token = auth_header.split(" ")[1]

    try:

        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM]
        )

        request.state.user_id = payload["user_id"]

    except Exception:

        raise HTTPException(status_code=401, detail="Invalid token")
