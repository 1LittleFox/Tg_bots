from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from random import randrange

from config import token_api

bot = Bot(token_api)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup()
b1 = KeyboardButton("/help")
b2 = KeyboardButton("/description")
b3 = KeyboardButton("/random")
e1 = KeyboardButton('❤️')
kb.add(b1, b2, b3).add(e1)

HELP_COMMAND = """
<b>/help</b> - <em>список комманд</em>
<b>/description</b> - <em>описание бота</em>
<b>/random_location</b> - <em>Пришлет случайную локацию</em>
<b>/❤️</b> - <em>Пришлет вам стикер</em>
"""


@dp.message_handler(commands=["start"])
async def help_comm(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="Начнем нашу работу!\nУ вас появились кнопки!",
                           parse_mode="HTML",
                           reply_markup=kb)


@dp.message_handler(commands=["help"])
async def help_comm(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=["description"])
async def help_comm(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="Этот бот пока что только на стадии разработки")
    await message.delete()


@dp.message_handler(commands=["random"])
async def send_random_point(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=randrange(1, 100),
                            longitude=randrange(1, 100))


@dp.message_handler()
async def help_comm(message: types.Message):
    if message.text == '❤️':
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker="CAACAgQAAxkBAAEJyLtkvUeJVjg71y1xSr3LU1T9UnWJxAACKQEAAmaa2yp9KH8g-qoZEi8E")


if __name__ == "__main__":
    executor.start_polling(dp)
