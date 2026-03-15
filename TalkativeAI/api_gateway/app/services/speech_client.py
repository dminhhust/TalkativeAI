import httpx
from app.config import *


async def transcribe_audio(file):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{SPEECH_SERVICE_URL}/speech/transcribe",
            files={"file": file}
        )

        return response.json()
