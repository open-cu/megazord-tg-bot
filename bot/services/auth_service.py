
import httpx
import logging
from config import EMAIL, PASSWORD, BASE_URL


async def get_token():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(BASE_URL+"auth/signin", json={"email": EMAIL, "password": PASSWORD})
            response.raise_for_status()
            data = response.json()
            return data.get("token")
        except httpx.HTTPStatusError as e:
            logging.error(f"Ошибка получения токена: {e}")
            return None
