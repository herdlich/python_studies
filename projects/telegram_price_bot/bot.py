import asyncio
from aiogram import Bot, Dispatcher, Router, html
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from pathlib import Path

from config import BOT_TOKEN

import monitor

router = Router()

path_csv_changes = Path("price_changes.csv")

ALLOWED_USERS = {}


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Hello. Im price monitor bot.\n"
        "Enter /help command to view the list of commands"
    )


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "Commands:\n"
        "/start\n"
        "/help\n"
        "/categories - list of available categories\n"
        "/monitor <category> — check price changes for category\n"
        "/id - find out your ID"
    )


@router.message(Command("monitor"))
async def monitor_handler(message: Message):
    if message.from_user.id not in ALLOWED_USERS:
        await message.answer("Access denied")
        return

    parts = message.text.split()

    if len(parts) < 2:
        await message.answer("Usage: /monitor <category>")
        return

    category = parts[1].lower()

    await message.answer(f"Monitoring started for category: {category}")

    result = await asyncio.to_thread(monitor.run_monitor, category)

    await message.answer(result)

    if result.startswith("Price changes found") and path_csv_changes.exists():
        report_file = FSInputFile(path_csv_changes)
        await message.answer_document(
            report_file,
            caption="Price changes report"
        )


@router.message(Command("id"))
async def id_handler(message: Message):
    user_id = message.from_user.id
    await message.answer(
        f"Your ID: <code>>{user_id}</code>",
        parse_mode=ParseMode.HTML
    )


@router.message(Command("categories"))
async def categories_handler(message: Message):
    if message.from_user.id not in ALLOWED_USERS:
        await message.answer("Access denied")
        return

    html_text = await asyncio.to_thread(monitor.download_html, monitor.BASE_URL)

    if not html_text:
        print("No HTML found")
        return

    categories = monitor.parse_categories(html_text)

    if not categories:
        await message.answer("No categories found")
        return

    text = "List of categories:\n"

    for category in categories:
        safe_category = html.quote(category['name'])
        text += f"• <code>{safe_category}</code>\n"

    await message.answer(text, parse_mode=ParseMode.HTML)


async def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is not set")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
