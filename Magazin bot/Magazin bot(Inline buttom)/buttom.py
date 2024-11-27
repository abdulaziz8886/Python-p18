from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlite3 import connect, Error  






def readProduct1():
    try:
        ulash = connect("restoran")
        cursor = ulash.cursor()
        cursor.execute("""Select * from maxsulotlar""")
        a = cursor.fetchall()
        return a
    except (Exception, Error) as error:
        print("Xato", error)
    finally:
        if ulash:
            cursor.close()
            ulash.close()




menyu_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Taomlar 🍔", callback_data="taom"), InlineKeyboardButton(text="Ishimliklar 🥂", callback_data="ichim")],
        [InlineKeyboardButton(text="Diser 🍰", callback_data="diser"), InlineKeyboardButton(text="Bog'lanish 📞", callback_data="boglan")],
        [InlineKeyboardButton(text="Zaqaz berish 🛒", callback_data="zaqaz"), InlineKeyboardButton(text="Reklama", callback_data="raklama")]
    ]
)
menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Taomlar 🍔", callback_data="taom"), InlineKeyboardButton(text="Ishimliklar 🥂", callback_data="ichim")],
        [InlineKeyboardButton(text="Diser 🍰", callback_data="diser"), InlineKeyboardButton(text="Bog'lanish 📞",callback_data="boglan")],
        [InlineKeyboardButton(text="Zaqaz berish 🛒", callback_data="zaqaz")]
    ]
)

ichim = InlineKeyboardBuilder()
for i in readProduct1():
    if i[2] == "ichim":
        ichim.button(text=f"{i[1]} -> {i[3]}", callback_data=i[1])
ichim.button(text="Orqaga 🔙", callback_data="orqaga 1")
ichim.adjust(2)

taom = InlineKeyboardBuilder()
for i in readProduct1():
    if i[2] == "taom":
        taom.button(text=f"{i[1]} -> {i[3]}", callback_data=i[1])
taom.button(text="Orqaga 🔙", callback_data="orqaga 1")
taom.adjust(2)

diser = InlineKeyboardBuilder()
for i in readProduct1():
    if i[2] == "diser":
        diser.button(text=f"{i[1]} -> {i[3]}", callback_data=i[1])
diser.button(text="Orqaga 🔙", callback_data="orqaga 1")
diser.adjust(2)

son = InlineKeyboardBuilder()
for i in range(1, 11):
    son.button(text=f"{i}", callback_data=f"{i}")
son.button(text="Orqaga 🔙", callback_data="orqaga 1")
son.adjust(5)
