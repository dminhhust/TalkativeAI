from fastapi import APIRouter
from app.services.auth_client import *

router = APIRouter()


@router.post("/register")
async def register(data: dict):

    return await register_user(data)


@router.post("/login")
async def login(data: dict):

    return await login_user(data)
