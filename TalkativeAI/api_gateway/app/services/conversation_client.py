import httpx
from app.config import *


async def send_message(payload):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{CONVERSATION_SERVICE_URL}/conversation/message",
            json=payload
        )

        return response.json()
