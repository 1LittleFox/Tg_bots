from aiogram import Bot, Dispatcher, executor, types

from config import token_api

bot = Bot(token_api)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_upper(message: types.Message):
    if message.text.count(' ') >= 1:
        await message.answer(text=message.text.upper()) #ответить на сообщение


if __name__ == "__main__":
    executor.start_polling(dp)
