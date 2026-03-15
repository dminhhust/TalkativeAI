from pydantic import BaseModel


class AnalyticsRequest(BaseModel):

    user_id: int
    session_id: int
    transcript: str
    emotions: list
    duration_seconds: float
