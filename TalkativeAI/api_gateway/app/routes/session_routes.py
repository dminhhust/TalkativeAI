from fastapi import APIRouter, Request, Depends
from app.middleware.auth_middleware import verify_auth
from app.services.analytics_client import *

router = APIRouter()


@router.get("/history")
async def get_history(
    request: Request,
    auth=Depends(verify_auth)
):

    user_id = request.state.user_id

    data = {"user_id": user_id}

    return await update_session_metrics(data)
