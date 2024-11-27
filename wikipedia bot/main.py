import asyncio
import logging
from aiogram import Dispatcher, Bot, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from config import bot_token as token
from sqlite3 import connect, Error
from aiogram.types import FSInputFile
import wikipedia
wikipedia.set_lang("uz")
def CreateObject():
    try:
        ulash = connect("Jadval")
        cursor = ulash.cursor()
        cursor .execute("""Create Table odamlar(
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
# CreateObject()
def create():
    try:
        ulash = connect("Jadval")
        cursor = ulash.cursor()
        cursor .execute("""Create Table sozlar(
                        username text not null,
                        user_id int not null,
                        sozi text not null
                        );""")
        ulash.commit()
    except (Exception, Error):
        print("Xato")
    finally:
        if ulash:
            cursor.close()
            ulash.close() 
create()
def addObject(ism, familiya, username, user_id):
    try:
        ulash = connect("Jadval")
        cursor = ulash.cursor()
        cursor.execute("""Insert into odamlar(ism, fam, username, user_id) values(?,?,?,?)""", (ism, familiya, username, user_id))
        ulash.commit()
    except (Exception, Error) as error:
        print("Xato1", error)
    finally:
        if ulash:
            cursor.close()
            ulash.close()
def add(username, user_id, sozi):
    try:
        ulash = connect("Jadval")
        cursor = ulash.cursor()
        cursor.execute("""Insert into sozlar(username, user_id, sozi) values(?,?,?)""", (username, user_id,sozi))
        ulash.commit()
    except (Exception, Error) as error:
        print("Xato2", error)
    finally:
        if ulash:
            cursor.close()
            ulash.close()
def readObject():
    try:
        ulash = connect("Jadval")
        cursor = ulash.cursor()
        cursor .execute("""select * from odamlar""")
        a = cursor.fetchall()
        return a
    except (Exception, Error):
        print("Xato3")
    finally:
        if ulash:
            cursor.close()
            ulash.close()
def read():
    try:
        ulash = connect("Jadval")
        cursor = ulash.cursor()
        cursor .execute("""select * from sozlar""")
        a = cursor.fetchall()
        return a
    except (Exception, Error):
        print("Xato4")
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
    await message.answer(f"Assalomu Alaykum: {ism}\nNima haqida malumot olmoqchisiz! ")

@db.message()
async def tanlov_1(message: Message):
    username = message.from_user.username
    user_id = message.from_user.id
    soz = message.text
    add(username=username, user_id=user_id, sozi=soz)
    malumot = wikipedia.summary(soz)
    await message.reply(f"Malumot\n\n{malumot}")
    

    
    
        


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

        
