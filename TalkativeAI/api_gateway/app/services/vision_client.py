import httpx
from app.config import *


async def analyze_face(frame):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{VISION_SERVICE_URL}/vision/emotion",
            files={"frame": frame}
        )

        return response.json()
