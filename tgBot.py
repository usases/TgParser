import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "7810183828:AAE9C3IULBLSXShg_RVCwtM7BZA2WMQp2C4"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_chat_id(message: Message):
    chat_id = str(message.chat.id).replace("-", "\\-")  # Экранирование
    await message.answer(f"Ваш кодID: {message.chat.id}")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())