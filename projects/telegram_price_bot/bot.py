import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

from config import BOT_TOKEN

from monitor import run_monitor

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
        "/status\n"
        "/monitor <category> — check price changes for category"
    )


@router.message(Command("status"))
async def status_handler(message: Message):
    await message.answer(
        "Bot is running ✅"
    )


@router.message(Command("monitor"))
async def monitor_handler(message: Message):
    parts = message.text.split()

    if len(parts) < 2:
        await message.answer("Usage: /monitor <category>")
        return

    category = parts[1]

    await message.answer(f"Monitoring started for category: {category}")

    result = await asyncio.to_thread(run_monitor, category)

    await message.answer(result)


async def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is not set")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
