from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🛒 ثبت سفارش"),
            ],
            [
                KeyboardButton(text="📞 پشتیبانی"),
            ]
        ],
        resize_keyboard=True
    )

    return keyboard
