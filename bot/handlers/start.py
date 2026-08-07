from bot.keyboards.main_menu import main_menu
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.database.database import add_user
from bot.utils.check_membership import check_membership


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    is_member = await check_membership(
        message.bot,
        message.from_user.id
    )

    if not is_member:
        await message.answer(
            "❌ برای استفاده از ربات ابتدا عضو کانال شوید:\n\n"
            "@mohrehmarradobargh"
        )
        return

    await add_user(
        user_id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username
    )

    await message.answer(
    "سلام 👋\n"
    "به ربات خوش آمدید.",
    reply_markup=main_menu()
)
