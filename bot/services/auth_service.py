import logging

import httpx

from bot.config import API_URL, SERVICE_EMAIL, SERVICE_PASSWORD


async def get_token():
    async with httpx.AsyncClient(base_url=API_URL) as client:
        try:
            response = await client.post(
                url="auth/signin",
                json={"email": SERVICE_EMAIL, "password": SERVICE_PASSWORD},
            )
            response.raise_for_status()
            data = response.json()
            return data.get("token")
        except httpx.HTTPStatusError as e:
            logging.error(f"Ошибка получения токена: {e}")
            return None
