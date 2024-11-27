from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ichimliklar 🥂"), KeyboardButton(text="Taomlar 🍟")],
        [KeyboardButton(text="Disert 🍰"), KeyboardButton(text="Jo'natish 🚚")]
    ], resize_keyboard=True,one_time_keyboard=True
)
contact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="contact ulashish ☎️", request_contact=True)],
        [KeyboardButton(text="Ortga 🔙")]
    ], resize_keyboard=True, one_time_keyboard=True
)
location = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Location 📍", request_location=True)],
        [KeyboardButton(text="Ortga 🔙")]
    ], resize_keyboard=True, one_time_keyboard=True
)