from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Пожалуйста, зарегистрируйтесь")

@router.message(Command(commands=["help"]))
async def cmd_start(message: types.Message):
    await message.answer("Платформа, которая позволяет администрировать командные соревнование в части создания и менеджмента команд")
