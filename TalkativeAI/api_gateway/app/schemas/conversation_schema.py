from pydantic import BaseModel


class MessageRequest(BaseModel):

    session_id: int
    message: str
    scenario: str
