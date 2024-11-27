from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from sqlite3 import connect, Error



admin = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kategorya qo'shish"), KeyboardButton(text="Maxsulot qoshish")],
        [KeyboardButton(text="Kategorya o'chirish"), KeyboardButton(text="Maxsulot o'chirish")],
        [KeyboardButton(text="User sifatida sinab ko'rish"), KeyboardButton(text="Reklama")],
        [KeyboardButton(text="Odamlar")]
    ], resize_keyboard=True, one_time_keyboard=True
)

menyu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Taom buyurtma berish"), KeyboardButton(text="Admin haqida malumot")],
    ], resize_keyboard=True, one_time_keyboard=True
)

orqaga = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Orqaga 🔙")]
    ], resize_keyboard=True, one_time_keyboard=True
)

tekshir2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ha"), KeyboardButton(text="Yoq")]
    ]
)

ichimlik = ReplyKeyboardBuilder()
