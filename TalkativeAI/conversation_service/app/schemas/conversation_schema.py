from pydantic import BaseModel


class ConversationRequest(BaseModel):

    user_id: int
    session_id: int
    message: str
    scenario: str
