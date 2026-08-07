from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text


router = Router()


@router.message(Text("📞 پشتیبانی"))
async def support_handler(message: Message):
    await message.answer(
        "📞 برای ارتباط با پشتیبانی پیام خود را ارسال کنید."
    )
