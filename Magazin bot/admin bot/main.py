from aiogram import Bot, F, Dispatcher
from aiogram.types import Message, CallbackQuery, KeyboardButton
import asyncio
import logging
from aiogram.filters.command import CommandStart
from config import token, Admin, User
from butom import admin, orqaga, menyu, tekshir2
from sqlite3 import connect, Error
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder


logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher()


def createCategory():
    try:
        ulash = connect("maxsulotlar")
        cursor = ulash.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS kategorya(
                    name text primary key not null
                    );
                       """)
        ulash.commit()
    except (Exception, Error) as error:
        print(f"Xato: \n\n{error}")
    finally:
        if ulash:
            cursor.close()
            ulash.close()

def createproduct():
    try:
        ulash = connect("maxsulotlar")
        cursor = ulash.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS maxsulot(
                    name text primary key not null,
                    narxi int not null,
                    rasmi text not null,
                    category_name text not null
                    );
                       """)
        ulash.commit()
    except (Exception, Error) as error:
        print(f"Xato1: \n\n{error}")
    finally:
        if ulash:
            cursor.close()
            ulash.close()
# createproduct()
def addCategor(name):
    try:
        ulash = connect("maxsulotlar")
        cursor = ulash.cursor()
        cursor.execute("""INSERT INTO kategorya(name) values(?);""", (name,))
        ulash.commit()
    except (Exception, Error) as error:
        print(f"Xato1.5: \n\n{error}")
    finally:
        if ulash:
            cursor.close()
            ulash.close()

def addproduct(name, narxi, rasmi, category_name):
    try:
        ulash = connect("maxsulotlar")
        cursor = ulash.cursor()
        cursor.execute("""INSERT INTO maxsulot(name, narxi, rasmi, category_name) values(?,?,?,?);""", (name, narxi, rasmi, category_name))
        ulash.commit()
    except (Exception, Error) as error:
        print(f"Xato2: \n\n{error}")
    finally:
        if ulash:
            cursor.close()
            ulash.close()

def readCategory():
    try:
        ulash = connect("maxsulotlar")
        cursor = ulash.cursor()
        cursor.execute("""Select * from kategorya""")
        a = cursor.fetchall()
        return a
    except (Exception, Error) as error:
        print(f"Xato3: \n\n{error}")
    finally:
        if ulash:
            cursor.close()
            ulash.close()

def readproduct():
    try:
        ulash = connect("maxsulotlar")
        cursor = ulash.cursor()
        cursor.execute("""Select * from maxsulot""")
        a = cursor.fetchall()
        return a
    except (Exception, Error) as error:
        print(f"Xato4: \n\n{error}")
    finally:
        if ulash:
            cursor.close()
            ulash.close()




def ForAdmin():


    def kategorya():  
        @dp.message(Admin.kategor)    
        async def kategorya2Bot(message:Message, state:FSMContext):
            xabar02 = message.text
            addCategor(name=xabar02)
            await message.answer("Muaffaqiyatli qo'shildi")
            await state.set_state(Admin.start)
    
    
    @dp.message(F.text == "Kategorya qo'shish")
    async def categoryaBot(message:Message, state:FSMContext):
        createCategory()
        await message.answer("Kategorya nomini kiriting")
        await state.set_state(Admin.kategor)
        kategorya()



    # Maxsulot qo'shish boshlandi   
    @dp.message(F.text == "Maxsulot qoshish")
    async def maxsulotBot(message:Message, state:FSMContext):
        buttom = ReplyKeyboardBuilder()
        for i in readCategory():
            buttom.button(text=f"{i[0]}")
        buttom.button(text="Orqaga 🔙")
        buttom.adjust(2)
        await message.answer("Qaysi kategoryaga qo'shmoqchisiz", reply_markup=buttom.as_markup(resize_keyboard=True, one_time_keyboard=True))
        await state.set_state(Admin.maxsulot)

    @dp.message(Admin.maxsulot)
    async def maxsulot1bot(message:Message, state:FSMContext):
        for i in readCategory():
            if i[0] == message.text:
                await state.update_data({"kategorya" : i[0]})
                await message.answer("Maxsulot nomini kiriting ",reply_markup=orqaga)
                await state.set_state(Admin.maxsulot_qosish)

    @dp.message(Admin.maxsulot_qosish)
    async def masulot_2_bor(message:Message, state:FSMContext):
        await state.update_data({"nomi" : message.text})
        await message.answer("Narxini kiriting 💸", reply_markup=orqaga)
        await state.set_state(Admin.maxsulot_nomi)



    @dp.message(Admin.maxsulot_nomi)
    async def masulot_3_bor(message:Message,  state:FSMContext):
        if message.text.isdigit():
            await state.update_data({"narxi" : message.text})
            await message.answer(f"Maxsulotingiz uchun rasm yuboring", reply_markup=orqaga)
            await state.set_state(Admin.maxsulot_rasm)
        else:
            await message.answer("❗️iltimos raqam ko'rinishida yozing❗️")    



    @dp.message(Admin.maxsulot_rasm)
    async def maxsulot4Bot(message:Message, state:FSMContext):
        try:
            await message.answer_photo(photo=message.text, caption="Rasmni tasdiqlaysizmi ✅", reply_markup=tekshir2)
            await state.update_data({"rasm": message.text})
            await state.set_state(Admin.maxsulot_tekshir2)
            print("AK")
        except:
            await message.answer("❗️Siz rasm yubormadiz❗️")
        

    @dp.message(Admin.maxsulot_tekshir2)
    async def tekBot(message:Message, state:FSMContext):
        xabar = message.text
        if xabar == "Ha":
            data = await state.get_data()
            await message.answer_photo(photo=data['rasm'], caption=f"Nomi: {data['nomi']}\nNarxi: {data['narxi']} so'm\nkategoryasi: {data['kategorya']}\nTasdiqlaysozmi ✅",reply_markup=tekshir2)
            await state.set_state(Admin.maxsulot_end)
        else:
            data =await state.get_data()
            data.pop('rasm', None)
            await state.update_data(data)
            await message.answer("Boshqa rasm yuborishingiz mumkin")

            await state.set_state(Admin.maxsulot_rasm)


    @dp.message(Admin.maxsulot_end)
    async def maxsulot5Bot(call:Message, state:FSMContext):
        xabar = call.text
        if xabar == "Ha":
            data = await state.get_data()
            addproduct(name=data['nomi'], narxi=data['narxi'], rasmi=data['rasm'], category_name=data['kategorya'])
            await call.answer("Muaffaqiyatli saqlandi", reply_markup=admin)
            
        else:
            await state.clear()
            await state.set_state(Admin.start)
    # MAXSULOT QOSHISH TUGADI




def forUser():
    @dp.message(F.text == "Taom buyurtma berish")
    async def tanlov(messege:Message, state:FSMContext):
        kategorya = ReplyKeyboardBuilder()
        for i in readCategory():
            kategorya.button(text=f"{i[0]}")
        kategorya.button(text="Orqaga 🔙")
        kategorya.adjust(2)
        await messege.answer(text="Kategorya tanlang",reply_markup=kategorya.as_markup(resize_keyboard=True, one_time_keyboard=True))
        await state.set_state(User.kategorya)

    @dp.message(User.kategorya)
    async def maxsulot(messege:Message, state:FSMContext):
        taom = ReplyKeyboardBuilder()
        for i in readproduct():
            if i[3] == messege.text:
                taom.button(text=i[0])
        taom.button(text="Orqaga 🔙")
        taom.adjust(2)
        await messege.answer("Maxsulot tanlang", reply_markup=taom.as_markup(resize_keyboard=True, one_time_keyboard=True))
        await state.set_state(User.maxsulot_soni)
    

    @dp.message(User.maxsulot_soni)
    async def maxsulot_soni(message:Message, state:FSMContext):
        await state.update_data({"nomi": message.text})
        await message.answer(f"{message.text}dan nechta")
        await state.set_state(User.finaly)

    @dp.message(User.finaly)
    async def end(message:Message, state:FSMContext):
        xabar = message.text
        if xabar.isdigit():
            await state.set_data({"soni":message.text})
            await message.answer("Buyurtma berildi\nYana biron narsa buyurasizmi?",reply_markup=menyu)
        else:
            await message.answer("Faqat raqam ko'rinishida buyurtma bering❗️")

    





@dp.message(CommandStart())
async def starbot(message:Message):
    print(message.from_user.id)
    if message.from_user.id == 5678926023:
        await message.answer(f"Assalomu Alaykum {message.from_user.full_name}\nsizga adminlik huquqi berilgan qo'shimcha funksiyalardan foydalanishingiz mummkin", reply_markup=admin)
        ForAdmin()
    else:
        await message.answer(f"Assalomu Alaykum {message.from_user.full_name}\nNima buyurtma berasiz",reply_markup=menyu)
        forUser()



@dp.message(F.text == "Orqaga 🔙")
async def orqa(message:Message, state:FSMContext):
    if F.chat_id == 5678926021:
        data = await state.get_data()
        data.clear()
        await message.answer("Bish saxifaga qaytdingiz", reply_markup=admin)
    else:
        await message.answer("Bish saxifaga qaytdingiz", reply_markup=menyu)





async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("Tugadi")