import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

from config import BOT_TOKEN

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Hello. Im price monitor bot.\n"
        "So far, i can respond to basic commands"
    )


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "Commands:\n"
        "/start\n"
        "/help\n"
        "/status"
    )


@router.message(Command("status"))
async def status_handler(message: Message):
    await message.answer(
        "Bot is running ✅"
    )


async def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is not set")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
