from fastapi import APIRouter, Request, Depends
from app.middleware.auth_middleware import verify_auth
from app.services.conversation_client import *

router = APIRouter()


@router.post("/message")
async def send_message(
    request: Request,
    data: dict,
    auth=Depends(verify_auth)
):

    user_id = request.state.user_id

    payload = {
        "user_id": user_id,
        **data
    }

    response = await send_message(payload)

    return response
