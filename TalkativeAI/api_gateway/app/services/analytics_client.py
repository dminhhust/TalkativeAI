import httpx
from app.config import *


async def update_session_metrics(data):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{ANALYTICS_SERVICE_URL}/analytics/update",
            json=data
        )

        return response.json()
