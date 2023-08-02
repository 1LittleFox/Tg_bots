from aiogram import Bot, Dispatcher, executor, types

from config import token_api

bot = Bot(token_api)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>список комманд</em>
<b>/give</b> - <em>присылает стикер с котом</em>
<b>/send_image</b> - <em>присылает фото</em>
/location
"""


async def on_startup(_):
    print('Я запустился!')


@dp.message_handler(commands=["give"])
async def send_cat(message: types.Message):
    await message.answer("Смотри какой смешной кот " + '❤️')
    await bot.send_sticker(chat_id=message.from_user.id, sticker="CAACAgIAAxkBAAEJwEZkuUdXxVeOvkcj3rMIPNRDMa96pgACAhYAAkmVOUl"
                                                         "-dsKxr46PpC8E")


@dp.message_handler(commands=["help"])
async def help_comm(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=["send_image"])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://proprikol.ru/wp-content/uploads/2020/09/kartinki-milyh-zhivotnyh-52.jpg")


@dp.message_handler(commands=["location"])
async def send_image(message: types.Message):
    await bot.send_location(chat_id=message.chat.id, latitude=60.00872651621342, longitude=30.258738135235255)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)

