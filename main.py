import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    WebAppInfo,
)

# Включаем логирование, чтобы в консоли хостинга было видно статус
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8716440491:AAHxy1MJ_FN6Q1NbRFc9hhK9wIv0GTZ8YQM"
WEBAPP_URL = "https://lehakozlov060814-droid.github.io/ai-tycoon-app/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎮 Играть в AI Tycoon",
                    web_app=WebAppInfo(url=WEBAPP_URL),
                )
            ]
        ]
    )
    await message.answer(
        "👋 **Добро пожаловать в AI Tycoon!**\n\n"
        "Нажмите кнопку ниже, чтобы открыть лабораторию нейросетей и начать обучение моделей:",
        reply_markup=keyboard,
        parse_mode="Markdown",
    )


async def main():
    # Сбрасываем очередь зависших сообщений
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
