from aiogram import Bot, Dispatcher, F
import asyncio
import logging
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import BOT_TOKEN as token
from buttom import menyu, menyu_admin, ichim, diser, taom, son
from sqlite3 import connect, Error
from datetime import datetime
from aiogram.utils.keyboard import InlineKeyboardBuilder
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
default=DefaultBotProperties(parse_mode=ParseMode.HTML)
bot = Bot(token=token)
shot_nomi = []
shot_soni = []


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


def readUser():
    try:
        ulash = connect("restoran")
        cursor = ulash.cursor()
        cursor.execute("""Select * from mijoz""")
        a = cursor.fetchall()
        return a
    except (Exception, Error) as error:
        print("Xato", error)
    finally:
        if ulash:
            cursor.close()
            ulash.close()
    

def addUser(full_name, user_id, user_name, date):
    try:
        ulash = connect("restoran")
        cursor = ulash.cursor()
        cursor.execute("""insert into users(ful_name, user_id, user_name, date) values(?,?,?,?)""", (full_name, user_id, user_name, date))
        ulash.commit()
        # return a
    except (Exception, Error) as error:
        print("Xato", error)
    finally:
        if ulash:
            cursor.close()
            ulash.close()


def readUser():
    try:
        ulash = connect("restoran")
        cursor = ulash.cursor()
        cursor.execute("""select * from users""")
        a = cursor.fetchall()
        return a
    except (Exception, Error) as error:
        print("Xato", error)
    finally:
        if ulash:
            cursor.close()
            ulash.close()

@dp.message(CommandStart())
async def StartBot(message:Message):
    fish = message.from_user.full_name
    user_id = message.from_user.id
    user_name = message.from_user.username
    addUser(full_name=fish, user_id=user_id, user_name=f"@{user_name}", date=datetime.now())
    if message.chat.id == 5678926023:
        await message.answer_photo(photo="https://astreae.kdcert.ru/uploads/files/sites/37/ZHQPjXgGmJ.png", caption=f"{message.from_user.full_name} Sizga adminlik huquqi berilgan!", reply_markup=menyu_admin)
        # await message.delete()
    else:
        await message.answer_photo(photo="https://astreae.kdcert.ru/uploads/files/sites/37/ZHQPjXgGmJ.png", caption=f"Assalomu alaykum {message.from_user.full_name}\nNima buyurtma berasiz", reply_markup=menyu)
        # await message.delete()


@dp.callback_query(F.data == "taom")
async def TaomlarBot1(cal: CallbackQuery):
    await cal.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=638b4b371fc8631ebc72fba28ac80e50_l-6961938-images-thumbs&n=13", reply_markup=taom.as_markup())
    await cal.message.delete()


@dp.callback_query(F.data == "ichim")
async def TaomlarBot2(cal: CallbackQuery):
    await cal.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=7bb66a95faac8765718e08e351081eac9ee3553b-7758299-images-thumbs&n=13", reply_markup=ichim.as_markup())
    await cal.message.delete()


@dp.callback_query(F.data == "diser")
async def TaomlarBot3(cal: CallbackQuery):
    await cal.message.answer_photo(photo="https://avatars.mds.yandex.net/get-mpic/4426104/img_id3631455626728817488.jpeg/orig", reply_markup=diser.as_markup())
    await cal.message.delete()


@dp.callback_query(F.data == "orqaga 1")
async def orqaga1(cal:CallbackQuery):
    await cal.message.answer_photo(photo="https://astreae.kdcert.ru/uploads/files/sites/37/ZHQPjXgGmJ.png", caption="Bosh sahifaga qaytdingiz", reply_markup=menyu)
    await cal.message.delete()


@dp.callback_query(F.data == "zaqaz")
async def zaqaz(cal:CallbackQuery):
    shot = ""
    cnt=0
    jami = 0
    for i in shot_nomi:
        for j in readProduct1():
            if j[1] == i:
                shot+=(f"{i}        {j[3]} so'mdan x {shot_soni[cnt]} = {int(j[3]) * int(shot_soni[cnt])}\n")
                jami+=int(j[3]) * int(shot_soni[cnt])
                cnt+=1
    # print(shot)
    await cal.message.answer(shot)
    await cal.message.answer(f"Jami: {jami}")
    await cal.message.delete()
    shot_nomi.clear()
    shot_soni.clear()

    
@dp.callback_query(F.data == "raklama")
async def reklamaBot(cal:CallbackQuery):
    if F.chat_id == 5678926023:
        await cal.message.answer(f"Reklama berish hizmani ishga tushdi.\nReklama uchun video, rasm, file, text yuborishingiz mumkin: ")
        @dp.message()
        async def reklama(message:Message):
            cnt = set()
            for i in readUser():
                cnt.add(i[1])
            for i in cnt:
                try:
                    await message.send_copy(chat_id=i)
                except Exception as error:
                    print(f"Hatolik: {error} foydalanuvchi idsi: {i}")
                
    else:
        await cal.message.answer("ha")









@dp.callback_query()
async def asos(cal:CallbackQuery):
    xabar = cal.data
    if xabar.isdigit():
        await cal.answer(f"{xabar} zakaz berdingiz")
        shot_soni.append(xabar)
        await cal.message.delete()
        await cal.message.answer_photo(photo="https://astreae.kdcert.ru/uploads/files/sites/37/ZHQPjXgGmJ.png", caption=f"Bosh sahifaga qaytdingiz {cal.from_user.full_name}", reply_markup=menyu)
    else:
        for i in readProduct1():
            if i[1] == xabar:
                await cal.message.answer_photo(photo=i[4],caption=f"Ismi: {xabar}\nNarxi: {i[3]}", reply_markup=son.as_markup())
                shot_nomi.append(xabar)
        await cal.message.delete()


async def main():
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print("Tugadi")