import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8504074176:AAGPg8H71gLAMDK1a8lpQU48UuyLbLm0itw"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("✅ Бот работает!")

if __name__ == "__main__":
    print("Бот запускается...")
    executor.start_polling(dp, skip_updates=True)
