from fastapi import APIRouter
from app.schemas.conversation_schema import *
from app.services.conversation_service import *

router = APIRouter()


@router.post("/message")
def send_message(data: ConversationRequest):

    response = process_message(
        data.user_id,
        data.session_id,
        data.message,
        data.scenario
    )

    return {"response": response}
