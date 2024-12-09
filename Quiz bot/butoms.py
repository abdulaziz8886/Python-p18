from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder
Buttom_admin = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="O'quvchilar natijalarini ko'rish 📊"), KeyboardButton(text="O'quvchilar ro'yxati 📋")],
        [KeyboardButton(text="Fan qo'shish 🆕"), KeyboardButton(text="Savol qo'shish 💡")],
        [KeyboardButton(text="Fan o'chirish 🗑️"), KeyboardButton(text="Savol o'chirish 🚮")],
        [KeyboardButton(text="Taklif va shikoyatlarni ko'rish 👀") ,KeyboardButton(text="User sifatida sinab ko'rish 🚀")]
    ], resize_keyboard=True, one_time_keyboard=True
)
Buttom_user_no = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kirish ➡️"), KeyboardButton(text="Ro'yxatdan o'tish ✍")],
        [KeyboardButton(text="Ushbu bot nima qila oladi 🤔?"), KeyboardButton(text="👨‍💻 Dasturchi bn boglanish ☎️")]
    ], resize_keyboard=True, one_time_keyboard=True
)
Buttom_user_yes = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Test ishlash 🎓"), KeyboardButton(text="Shaxsiy statistikani ko'rish 👀")],
        [KeyboardButton(text="Login o'zgartirish 🛠️"), KeyboardButton(text="Parolni almashtirish ⚙️")],
        [KeyboardButton(text="Taklif yoki shikoyat qilish"), KeyboardButton(text="👨‍💻 Dasturchi bn bog'lanish ☎️")],
        [KeyboardButton(text="Chiqish 🔙")]
    ], resize_keyboard=True, one_time_keyboard=True
)
buttom_orqa = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Orqaga 🔙")]
    ],resize_keyboard=True, one_time_keyboard=True
)
Buttom_tekshir = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ha 👍", callback_data="ha"), InlineKeyboardButton(text="Yoq 👎",callback_data="yoq")]
    ]
)
cantoct = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Cantact ulashish ☎️", request_contact=True)]
    ],resize_keyboard=True, one_time_keyboard=True
)
parol_almashtir = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Parolim esimda yoq 😢")]
    ],resize_keyboard=True, one_time_keyboard=True
)

parol_almashtir_1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Parolim yodimda yoq 😢")]
    ],resize_keyboard=True, one_time_keyboard=True
)



fan_tekshir = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text="Orqaga 🔙", callback_data="Orqaga 🔙"), InlineKeyboardButton(text="Keyingi savol ▶️", callback_data="keyingi savol ▶️")]
    ]
)