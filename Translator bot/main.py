import asyncio
import logging
from aiogram import Dispatcher, Bot, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from config import BOT_TOKEN as token
from sqlite3 import connect, Error
from aiogram.types import FSInputFile
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
tr = GoogleTranslator(source="auto", target="en")

def CreateObject():
    try:
        ulash = connect("Jadval")
        cursor = ulash.cursor()
        cursor .execute("""Create Table malumotlar(
                        ism text not null,
                        fam text,
                        username text not null,
                        user_id int primary key not null
                        );""")
        ulash.commit()
    except (Exception, Error):
        print("Xato")
    finally:
        if ulash:
            cursor.close()
            ulash.close()      
CreateObject()
def addObject(ism, familiya, username, user_id):
    try:
        ulash = connect("Jadval")
        cursor = ulash.cursor()
        cursor.execute("""Insert into malumotlar(ism, fam, username, user_id) values(?,?,?,?)""", (ism, familiya, username, user_id))
        ulash.commit()
    except (Exception, Error) as error:
        print("Xato")
    finally:
        if ulash:
            cursor.close()
            ulash.close()
def readObject():
    try:
        ulash = connect("Jadval")
        cursor = ulash.cursor()
        cursor .execute("""select * from malumotlar""")
        a = cursor.fetchall()
        return a
    except (Exception, Error):
        print("Xato")
    finally:
        if ulash:
            cursor.close()
            ulash.close()
cnt = []
db = Dispatcher()
bot = Bot(token=token,default = DefaultBotProperties(parse_mode=ParseMode.HTML))
logging.basicConfig(level=logging.INFO)


@db.message(CommandStart())
async def start(message:Message):
    ism = message.from_user.first_name
    fam = message.from_user.last_name
    username = message.from_user.username
    user_id = message.from_user.id
    addObject(ism=ism, familiya=fam,username=username, user_id=user_id)
    await message.answer(f"Assalomu Alaykum: {ism}\nTarjima qilmoqchi bo'lgan so'zni yuboring! ")

@db.message()
async def tanlov_1(message: Message):
    user_id = message.from_user.id
    tarjima = tr.translate(message.text)
    await message.reply(tarjima)
    voise = gTTS(tarjima)
    voise.save("ovoz.mp3") 
    await message.reply_audio(audio=FSInputFile("ovoz.mp3"))
    os.remove("ovoz.mp3")

    

    
    
        


@db.message(Command("users"))
async def users(message:Message):
    for i in readObject():
        await message.answer(f"Ismi: {i[0]}\nFamiliyasi: {i[1]}\nUsername: {i[2]}\nID: {i[3]}")

@db.message(Command("reklama"), F.from_user.id == 5678926023)
async def ReklamaPost(message: Message):
    for id in readObject():
        await message.answer("Python p 18 guruhidan reklama")



async def main():
    await db.start_polling(bot)
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("tugadi")

        
