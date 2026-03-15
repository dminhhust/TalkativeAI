import httpx
from app.config import *


async def register_user(data):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{AUTH_SERVICE_URL}/auth/register",
            json=data
        )

        return response.json()


async def login_user(data):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{AUTH_SERVICE_URL}/auth/login",
            json=data
        )

        return response.json()
