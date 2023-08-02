from aiogram import Bot, Dispatcher, executor, types
from inlineKeybord import ikb, kb

from config import token_api

bot = Bot(token_api)
dp = Dispatcher(bot)


async def on_startup(_):
    print("Я запустился!")


@dp.message_handler(commands=["start"])
async def start_comm(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать в наш <b>Бот!</b>"
                                "\nУ вас появилась клавиатура!",
                           parse_mode="HTML",
                           reply_markup=kb)


@dp.message_handler(commands=["links"])
async def start_comm(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Посмотрите это видео!",
                           parse_mode="HTML",
                           reply_markup=ikb)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

