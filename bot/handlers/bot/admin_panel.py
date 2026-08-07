from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.config import ADMIN_ID


router = Router()


@router.message(Command("panel"))
async def admin_panel(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        "👨‍💻 پنل مدیریت\n\n"
        "📊 آمار\n"
        "📢 ارسال همگانی"
    )
