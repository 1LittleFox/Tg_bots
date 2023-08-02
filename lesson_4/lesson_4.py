from aiogram import Bot, Dispatcher, executor, types

import string
import random

from config import token_api

bot = Bot(token_api)
dp = Dispatcher(bot)

count = 0


@dp.message_handler(commands=["description"])
async def description_command(message: types.Message):
    await message.answer('Этот бот умеет отправлять случайные символы латинского алфавита')
    await message.delete()


@dp.message_handler(commands=["count"])
async def check_count(message: types.Message):
    global count
    await message.answer(f'Count: {count}')
    count += 1


@dp.message_handler()
async def check_zero(message: types.Message):
    if '0' in message.text:
        await message.reply('YES')
    else:
        await message.reply('NO')


@dp.message_handler()
async def send_random_latter(message: types.Message):
    await message.reply(random.choice(string.ascii_letters))


if __name__ == "__main__":
    executor.start_polling(dp)
