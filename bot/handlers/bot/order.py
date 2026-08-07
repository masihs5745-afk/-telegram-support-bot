from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text


router = Router()


@router.message(Text("🛒 ثبت سفارش"))
async def order_start(message: Message):
    await message.answer(
        "لطفاً نوع سفارش خود را وارد کنید:"
    )
