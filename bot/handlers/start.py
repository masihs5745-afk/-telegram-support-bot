from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.database.database import add_user


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await add_user(
        user_id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username
    )

    await message.answer(
        "سلام 👋\n"
        "به ربات خوش آمدید."
    )
