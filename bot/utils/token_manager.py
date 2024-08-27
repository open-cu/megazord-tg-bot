import logging

import httpx

from bot.config import API_URL
from bot.services.auth_service import get_token


class TokenManager:
    def __init__(self):
        self.token = None

    async def get_token(self):
        if self.token is None:
            self.token = await get_token()
        return self.token

    async def refresh_token(self):
        logging.info("Обновление токена...")
        self.token = await get_token()
        return self.token

    async def request_with_token(self, method: str, url: str, **kwargs):
        token = await self.get_token()

        headers = kwargs.get("headers", {})
        headers["Authorization"] = f"Bearer {token}"
        kwargs["headers"] = headers

        async with httpx.AsyncClient(base_url=API_URL) as client:
            response = await client.request(method=method, url=url, **kwargs)

            if response.status_code == 401:
                logging.info("Токен устарел. Обновляем токен...")
                await self.refresh_token()
                headers["Authorization"] = f"Bearer {self.token}"
                response = await client.request(method=method, url=url, **kwargs)

            return response
