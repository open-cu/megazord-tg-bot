import sys
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import BOT_TOKEN
from handlers import registration

logging.basicConfig(level=logging.INFO)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота 🚀"),
        BotCommand(command="/help", description="Помощь ℹ️"),
    ]
    await bot.set_my_commands(commands)

async def on_startup(bot: Bot, dp: Dispatcher):
    await set_commands(bot)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(registration.router)

    await on_startup(bot, dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
