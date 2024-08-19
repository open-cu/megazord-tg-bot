import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from config import BOT_TOKEN
from handlers import registration
from utils.token_manager import TokenManager

logging.basicConfig(level=logging.INFO)

token_manager = TokenManager()

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать диалог 🤖"),
        BotCommand(command="/help", description="Помощь ℹ️"),
    ]
    await bot.set_my_commands(commands)

async def on_startup(bot: Bot, dp: Dispatcher):
    await set_commands(bot)
    await token_manager.refresh_token()  # Принудительное обновление токена при старте

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(registration.router)
    await on_startup(bot, dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
