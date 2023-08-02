from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


"""Inline клавиатура"""
ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Button 1',
                           url="https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr"
                               "&index=11")
ib2 = InlineKeyboardButton(text='Button 2',
                           url="https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr"
                               "&index=11")
ib3 = InlineKeyboardButton(text='Button 3',
                           url="https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr"
                               "&index=11")
ib4 = InlineKeyboardButton(text='Button 4',
                           url="https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr"
                               "&index=11")

ikb.add(ib1).insert(ib2).add(ib3).add(ib4)

"""Обычная клавиатура"""
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/links')


kb.add(b1)