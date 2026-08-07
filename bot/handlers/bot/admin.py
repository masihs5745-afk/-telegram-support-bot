from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def admin_reply_handler(message: Message):
    pass
