import logging
from urllib.parse import urljoin

import httpx
from config import API_URL, EMAIL, PASSWORD


async def get_token():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                urljoin(API_URL, "auth/signin"),
                json={"email": EMAIL, "password": PASSWORD},
            )
            response.raise_for_status()
            data = response.json()
            return data.get("token")
        except httpx.HTTPStatusError as e:
            logging.error(f"Ошибка получения токена: {e}")
            return None
