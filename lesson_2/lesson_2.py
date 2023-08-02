from aiogram import Bot, Dispatcher, executor, types

from config import token_api

HELP_COMMAND = """
help - список комманд\nstart - начать работу с ботом
"""

bot = Bot(token_api)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="Hello, it's telegram Bot!")
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp)
