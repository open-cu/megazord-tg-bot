import logging
from aiogram import Router, types
from aiogram.filters import Command
from config import BASE_URL
from utils.token_manager import TokenManager

router = Router()

token_manager = TokenManager()  # Создаем экземпляр TokenManager

@router.message(Command("start"))
async def start(message: types.Message):
    command_with_args = message.text.split()

    if len(command_with_args) < 2:
        await message.answer("👋 Привет! Этот бот предназначен для отправки уведомлений участникам хакатонов.")
        return

    user_uuid = command_with_args[1]  # Получаем UUID напрямую

    if not user_uuid:
        await message.answer("Упс! 😅 Кажется, не удалось найти тебя. Попробуй еще раз!")
        return

    telegram_id = message.from_user.id

    try:
        response = await token_manager.request_with_token(
            method="POST",
            url=f"{BASE_URL}link_telegram",
            params={"user_id": user_uuid, "telegram_id": telegram_id},  # Передаем как параметры запроса
            headers={"accept": "application/json"}
        )

        if response.status_code == 200:
            await message.answer(
                "🎉 Ура! Твой Telegram ID успешно привязан к аккаунту. Теперь мы сможем держать тебя в курсе всех событий! 🚀")
        else:
            await message.answer("Ой! 😕 Что-то пошло не так... Попробуй еще раз чуть позже.")
    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await message.answer("❌ Произошла ошибка. Пожалуйста, попробуйте снова позже.")
