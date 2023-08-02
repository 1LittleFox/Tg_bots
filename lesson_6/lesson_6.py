from aiogram import Bot, Dispatcher, executor, types

from config import token_api

bot = Bot(token_api)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>список комманд</em>\n<b>/give</b> - <em>присылает стикер с котом</em>
"""


async def on_startup(_):
    print('Я запустился!')


@dp.message_handler(commands=["give"])
async def send_cat(message: types.Message):
    await message.reply("Смотри какой смешной кот " + '❤️')
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJwEZkuUdXxVeOvkcj3rMIPNRDMa96pgACAhYAAkmVOUl"
                                                         "-dsKxr46PpC8E")


@dp.message_handler(commands=["help"])
async def help_comm(message: types.Message):
    await message.reply(text=HELP_COMMAND, parse_mode="HTML")


@dp.message_handler(content_types=["sticker"])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler()
async def send_count_emoji2(message: types.Message):
    await message.answer(text=str(message.text.count('😘')))


#@dp.message_handler()
#async def send_count_emoji1(message: types.Message):
#    count = 0
#    for letters in message.text:
#        if letters == '😘':
#           count += 1
#    await message.reply(f"В вашем сообщении {count} 😘")
#
#
#@dp.message_handler()
#async def send_black(message: types.Message):
#    if message.text == '❤️':
#        await message.answer('🖤 ')


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
