import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, WebAppInfo

# Считываем токен и ссылку из переменных окружения (или укажите строкой)
BOT_TOKEN = os.getenv("BOT_TOKEN", "ВАШ_ТОКЕН_BOTFATHER")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://lehakozlov060814-droid.github.io/название-репозитория/")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎮 Играть в AI Tycoon",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )
    await message.answer(
        "👋 **AI Tycoon**\n\n"
        "Нажми кнопку ниже, чтобы открыть лабораторию и начать обучать модели:",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
