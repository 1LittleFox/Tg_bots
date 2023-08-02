from aiogram import Bot, Dispatcher, executor, types


from config import token_api

bot = Bot(token_api)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот был успешно запущен!')


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer('<em>Привет, <b>добро</b> пожаловать в наш бот!</em>', parse_mode="HTML")


@dp.message_handler(commands=["sticker"])
async def send_sticker(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJwEZkuUdXxVeOvkcj3rMIPNRDMa96pgACAhYAAkmVOUl"
                                                         "-dsKxr46PpC8E")
    await message.delete()


@dp.message_handler()
async def send_emoji(message: types.Message):
    await message.answer(message.text + '❤️')


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)