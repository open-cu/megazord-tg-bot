from aiogram import Router, types, Dispatcher, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

router = Router()

class RegistrationState(StatesGroup):
    waiting_for_email = State()
    waiting_for_code = State()

@router.message(Command(commands=["start"]))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("👋 Добро пожаловать! Пожалуйста, введите вашу почту 📧")
    await state.set_state(RegistrationState.waiting_for_email)

@router.message(RegistrationState.waiting_for_email)
async def process_email(message: types.Message, state: FSMContext, bot: Bot):
    email = message.text
    # Сохраните email в состоянии
    await state.update_data(email=email)

    # Генерация и отправка кода на email (реализуйте отправку кода)
    code = "123456"  # Пример кода, замените на генерацию и отправку реального кода
    await bot.send_message(message.chat.id, f"📧 Код отправлен на почту: {email} ✅")

    # Переход к следующему состоянию
    await state.set_state(RegistrationState.waiting_for_code)

@router.message(RegistrationState.waiting_for_code)
async def process_code(message: types.Message, state: FSMContext, bot: Bot):
    user_data = await state.get_data()
    correct_code = "123456"  # Пример кода, замените на реальный код

    if message.text == correct_code:
        await message.answer("🎉 Код подтвержден! Регистрация завершена ✅")
        await state.clear()
    else:
        await message.answer("❌ Неверный код.")
        # Генерация и отправка нового кода
        new_code = "654321"  # Пример нового кода
        await bot.send_message(message.chat.id, f"🔄 Новый код отправлен на почту {user_data['email']} 📧")
        # Сохраняем новый код для последующей проверки
        await state.update_data(correct_code=new_code)
