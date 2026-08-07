from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.config import ADMIN_ID
from bot.database.database import get_users_count, get_orders_count


router = Router()


@router.message(Command("panel"))
async def admin_panel(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    users = await get_users_count()
    orders = await get_orders_count()

    await message.answer(
        "👨‍💻 پنل مدیریت\n\n"
        f"👥 تعداد کاربران: {users}\n"
        f"📦 تعداد سفارش‌ها: {orders}\n\n"
        "📢 ارسال همگانی به‌زودی اضافه می‌شود."
    )
