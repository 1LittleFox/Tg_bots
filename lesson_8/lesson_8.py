from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import token_api

bot = Bot(token_api)
dp = Dispatcher(bot)


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/photo')
kb.add(b1).insert(b2).add(b3)


HELP_COMMAND = """
<b>/help</b> - <em>список комманд</em>
<b>/start</b> - <em>Старт работы с ботом</em>
<b>/description</b> - <em>присылает фото</em>
<b>/photo</b> - <em>присылает локацию</em>
"""


async def on_startup(_):
    print('Я запустился!')


@dp.message_handler(commands=["help"])
async def help_comm(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML",
                           )
    await message.delete()


@dp.message_handler(commands=["start"])
async def start_comm(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать в наш <b>Бот!</b>",
                           parse_mode="HTML",
                           reply_markup=kb)


@dp.message_handler(commands=["description"])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Наш бот умеет отправлять фото",
                           parse_mode="HTML")


@dp.message_handler(commands=["photo"])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://proprikol.ru/wp-content/uploads/2020/09/kartinki-milyh-zhivotnyh-52.jpg")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)

