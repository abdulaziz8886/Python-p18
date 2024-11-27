import asyncio
import logging
from aiogram import Dispatcher, Bot, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
# from aiogram.filters import Text
from config import BOT_TOKEN as token
from sqlite3 import connect, Error
from buttom import menu, contact, location
from aiogram.utils.keyboard import ReplyKeyboardBuilder
shot_name = []
shot_son =  [] 
tel = []  
def addMijoz(name, user_name, user_id, tell, lat, long, daromad):
    try:
        ulash = connect("restoran")
        cursor = ulash.cursor()
        cursor.execute("""insert into mijoz(name, user_name, user_id, tell, lat, long, daromad) values(?,?,?,?,?,?,?)""", (name, user_name, user_id, tell, lat, long, daromad))
        ulash.commit()
    except (Exception, Error) as error:
        print("Xato", error)
    finally:
        if ulash:
            cursor.close()
            ulash.close()

def readProduct():
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


db = Dispatcher()
bot = Bot(token=token,default = DefaultBotProperties(parse_mode=ParseMode.HTML))
logging.basicConfig(level=logging.INFO)


@db.message(F.text == "Ortga 🔙")
async def tekshir(message:Message):
    await message.answer("✅Muffaqiyatli ortga qaytarildi?", reply_markup=menu)


@db.message(F.text.endswith("."))
async def toti(message: Message):
    for i in message.text:
        shot_son.append(i[0])
    await message.answer("🤵🏻Muvaffaqiyatli qabul qilindi yana biron narsa buyurasizmi? ", reply_markup=menu)
    

@db.message(F.contact)
async def contac(message: Message):
    tel.append(message.contact.phone_number)
    if message.contact.user_id == message.from_user.id:
        await message.reply("Sizning telefon raqqaminiz muaffaqiyatli saqlandi✅:", reply_markup=location)
        await message.answer("Turgan joyingizni belgilang! 🗺")
    else:
        await message.reply(f"Iltimos shaxsiy raqaminizni taqdim qiling 🚫" , reply_markup=contac)

@db.message(F.location)
async def LocationBot(message: Message):
    ism = message.from_user.full_name
    user_ism = message.from_user.username
    user_id = message.from_user.id
    nomer = tel[0]
    tel.pop(0)
    la = message.location.latitude
    lo = message.location.longitude

    await message.answer("Locatsiya saqlandi")
    cnt = 0
    jami = 0
    for i in shot_name:
        for j in readProduct():
            if j[1] == str(i[0]):
                await message.answer(f"{i[0]}    {j[3]}  x   {shot_son[cnt]} = {int(j[3]) * int(shot_son[cnt])}")
                jami+=int(j[3]) * int(shot_son[cnt])
    
        cnt+=2
    await message.answer(f"Jami: {jami}so'm")
    addMijoz(name=ism,user_name=f"@{user_ism}",user_id=user_id,tell=f"+998{nomer}",lat=la,long=lo,daromad=jami)
@db.message(F.text == "Boshqa")
async def boshqa(message:Message):
    boshqacha = ReplyKeyboardBuilder()
    for i in range(1,101):
        boshqacha.button(text=str(f"{i}."))
    boshqacha.button(text="??Ortga")
    boshqacha.adjust(10)
    await message.answer(f"Marxamat: nechta buyurtma berasiz?",reply_markup=boshqacha.as_markup(resize_keyboard=True, one_time_keyboard=True))


@db.message(F.text == "Jo'natish 🚚")
async def zaqaz(message:Message):
    await message.answer("Cantacni yuboring 📞", reply_markup=contact)


@db.message(CommandStart())
async def startBot(message: Message):
    await message.answer(f"🤵🏻 Asssalomu Alaykum {message.from_user.full_name}\nNime buyurtma berasiz", reply_markup=menu)
    

@db.message(F.text == "Ichimliklar 🥂")
async def amal(message: Message):
    taom = ReplyKeyboardBuilder()
    for i in readProduct():
        if i[2] == "Ichimliklar":
            taom.button(text=f"{i[1]} -> {i[3]} so'm")
    taom.button(text=f"Ortga 🔙")
    taom.adjust(2)
    await message.answer("🤵🏻 Nima buyurtma berasiz: ",reply_markup=taom.as_markup(resize_keyboard=True, one_time_keyboard=True))

@db.message(F.text == "Taomlar 🍟")
async def amal(message: Message):
    taom = ReplyKeyboardBuilder()
    for i in readProduct():
        if i[2] == "Taomlar":
            taom.button(text=f"{i[1]} -> {i[3]} so'm")
    taom.button(text=f"Ortga 🔙")
    taom.adjust(2)
    await message.answer("Tanla",reply_markup=taom.as_markup(resize_keyboard=True, one_time_keyboard=True))
    
@db.message(F.text == "Disert 🍰")
async def amal(message: Message):
    taom = ReplyKeyboardBuilder()
    for i in readProduct():
        if i[2] == "Disert":
            taom.button(text=f"{i[1]} -> {i[3]} so'm")
    taom.button(text=f"Ortga 🔙")
    taom.adjust(2)
    await message.answer("Tanla",reply_markup=taom.as_markup(resize_keyboard=True, one_time_keyboard=True))

@db.message()
async def son(message: Message):
    if "->" in message.text:
        a = message.text.split()
        shot_name.append(a)
        son = ReplyKeyboardBuilder()
        for i in range(1,10):
            son.button(text=str(f"{i}."))
        son.button(text="Boshqa")
        son.button(text="Ortga 🔙")
        son.adjust(3)
        await message.answer(f"🤵🏻 {a[0]}dan nechta",reply_markup=son.as_markup(resize_keyboard=True, one_time_keyboard=True))
        



    
    

async def main():
    await db.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("tugadi")
