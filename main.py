import os
import asyncio
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

load_dotenv()

BOT_TOKEN = os.getenv("8716431132:AAGvQBMGUl4HrVdamxmYZFjTOVFVcoi_Dlo")

bot = Bot(token=8716431132:AAGvQBMGUl4HrVdamxmYZFjTOVFVcoi_Dlo)
dp = Dispatcher()


async def main():
    print("Bot is starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
