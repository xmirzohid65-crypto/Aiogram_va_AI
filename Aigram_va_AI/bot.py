import asyncio
import os

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

from database import create_table, add_user

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    user = message.from_user

    await add_user(
        user_id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username
    )

    await message.answer(
        f"Salom, {user.first_name}!\n"
        "Sizning ma'lumotlaringiz bazaga saqlandi."
    )


async def main():
    await create_table()

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())