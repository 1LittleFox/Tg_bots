from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from config import token_api

bot = Bot(token_api)
dp = Dispatcher(bot)


kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = KeyboardButton(text="/help")
kb2 = KeyboardButton(text="/vote")

kb.add(kb1, kb2)


async def on_start(_):
    print("I have been started up")


@dp.message_handler(commands=["start"])
async def start_comm(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Welcome!",
                           reply_markup=kb)


@dp.message_handler(commands=['vote'])
async def start_comm(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ikb1 = InlineKeyboardButton(text="Yes",
                                callback_data='Like')
    ikb2 = InlineKeyboardButton(text="No",
                                callback_data='disLike')
    ikb.add(ikb1, ikb2)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://www.tapeciarnia.pl/tapety/normalne/178919_mlyn_wodny_rzeka_kamienie_las.jpg",
                         caption="Нравится ли тебе данная фотография",
                         reply_markup=ikb)


@dp.callback_query_handler()
async def vote_calling(callback: types.CallbackQuery):
    if callback.data == 'Like':
        return await callback.bot.send_message(chat_id=callback.from_user.id,
                                               text="Спасибо что оценили:)")
    await callback.answer('Что вам не понравилось?')

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           on_startup=on_start)
