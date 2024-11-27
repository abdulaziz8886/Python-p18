from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menyu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Sherik kerak"), KeyboardButton(text="Ish joyi kerak")],
        [KeyboardButton(text="Shogird kerak"), KeyboardButton(text="Ustoz kerak")]
    ], resize_keyboard=True, one_time_keyboard=True
)

tekshir1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ha 👍", callback_data="ha"), InlineKeyboardButton(text="Yoq 👎", callback_data="yoq")]
    ]
)