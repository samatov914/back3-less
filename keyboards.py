from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

inline_buttons = [
    InlineKeyboardButton('Старт', callback_data='start'),
    InlineKeyboardButton('Помощь', callback_data='help'),
    InlineKeyboardButton('Скачать видео', callback_data='video'),
    InlineKeyboardButton('Скачать аудио', callback_data='audio'),
    InlineKeyboardButton('Отправить свой номер телефона', callback_data='share')
]

button = InlineKeyboardMarkup().add(*inline_buttons)

share_keyboards = [
    KeyboardButton('Поделиться номером', request_contact=True),
    KeyboardButton('Отправить локацию', request_location=True)
]

share_button = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(*share_keyboards)