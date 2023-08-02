from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import token_api

bot = Bot(token_api)
dp = Dispatcher(bot)


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Button 1',
                           url="https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=11")
ib2 = InlineKeyboardButton(text='Button 2',
                           url="https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=11")

ikb.add(ib1, ib2)

@dp.message_handler(commands=["start"])
async def start_comm(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать в наш <b>Бот!</b>",
                           parse_mode="HTML",
                           reply_markup=ikb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

