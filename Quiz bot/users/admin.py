from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import CommandStart
from state import *
from CRUD import *
from butoms import *
from config import token

bot = Bot(token=token)

admin_router = Router()
admins = [5678926023]


@admin_router.message(CommandStart())
async def startBot(message:Message):
    if message.from_user.id in admins:
        await message.answer(f"Assalomu Alaykum {message.from_user.full_name}\nSizga adminlik huquqi berilgan", reply_markup=Buttom_admin)
    else:
        user_id = str(message.from_user.id)
        users = readlogin()
        for i in users:
            if user_id == str(i[2]):
                if i[-1].lower() == "y":
                    await message.answer(f"Assalomu Alaykum {message.from_user.full_name}", reply_markup=Buttom_user_yes)
                else:
                    await message.answer(f"Assalomu Alaykum {message.from_user.full_name}", reply_markup=Buttom_user_no)
                return
            
        await message.answer("☹️ Afsuski, sizda akkaunt mavjud emas.'Ro'yxatdan o'tish ✍️' tugmasi orqali akkaunt yaratishingiz mumkin.",reply_markup=Buttom_user_no)


@admin_router.message(F.text == "Orqaga 🔙")
async def orqaBot(message:Message, state:FSMContext):
    await state.clear()
    user_id = message.from_user.id
    if user_id in admins:
        await message.answer(f"Bosh saxifaga qaytdingiz", reply_markup=Buttom_admin)
    else:
        for i in readlogin():
            if str(user_id) in i[2]:
                if i[-1].lower() == "y":
                    await message.answer("Bosh saxifaga qaytdingiz", reply_markup=Buttom_user_yes)
                else:
                    await message.answer("Bosh saxifaga qaytdingiz", reply_markup=Buttom_user_no)


@admin_router.callback_query(F.data == "Orqaga 🔙")
async def orqa2Bot(cal:CallbackQuery, state:FSMContext):
    await state.clear()
    user_id = cal.from_user.id
    if user_id in admins:
        await cal.message.answer(f"Bosh saxifaga qaytdingiz", reply_markup=Buttom_admin)
    else:
        for i in readlogin():
            if str(user_id) in i[2]:
                if i[-1].lower() == "y":
                    await cal.message.answer("Bosh saxifaga qaytdingiz", reply_markup=Buttom_user_yes)
                else:
                    await cal.message.answer("Bosh saxifaga qaytdingiz", reply_markup=Buttom_user_no)




a = set()
@admin_router.message(F.text =="O'quvchilar ro'yxati 📋")
async def royxatBot(message:Message, state:FSMContext):
    user = InlineKeyboardBuilder()
    for i in readlogin():
        a.add(i[1])
    for i in a:
        user.button(text=i, callback_data=i)
    user.button(text="Orqaga 🔙", callback_data="Orqaga 🔙")
    user.adjust()
    await message.answer("Foydalanuvchi tanlang", reply_markup=user.as_markup())
    await state.set_state(foydalanuvchi.user)

@admin_router.callback_query(foydalanuvchi.user)
async def foydaBot(cal:CallbackQuery, state:FSMContext):
    xabar = cal.data
    for i in readlogin():
        if str(i[1]) == str(xabar):
            await cal.message.answer(f"Ismi: {i[0]}\nUser_name: {i[1]}\ntell: +{i[3]}\nLogini: {i[4]}", reply_markup=Buttom_admin)
    await state.clear()



b = set()
@admin_router.message(F.text =="O'quvchilar natijalarini ko'rish 📊")
async def royxatBot(message:Message, state:FSMContext):
    user1 = InlineKeyboardBuilder()
    for i in readusers():
        b.add(i[1])
    for i in b:
        user1.button(text=i, callback_data=i)
    user1.button(text="Orqaga 🔙", callback_data="Orqaga 🔙")
    user1.adjust()
    await message.answer("Foydalanuvchi tanlang", reply_markup=user1.as_markup())
    await state.set_state(foydalanuvchi.finish)

@admin_router.callback_query(foydalanuvchi.finish)
async def foydaBot(cal:CallbackQuery, state:FSMContext):
    xabar = cal.data
    for i in readusers():
        if str(i[1]) == str(xabar):
            await cal.message.answer(f"Ismi: {i[0]}\nUser_name: {i[1]}\nBerilgan savollar soni: {i[3]}\nTo'g'ri javob berilgan savollar soni: {i[4]}\nFoizi : {i[5]}", reply_markup=Buttom_admin)
    await state.clear()




@admin_router.message(F.text == "Fan qo'shish 🆕")
async def fanQoshBot(message:Message, state:FSMContext):
    await message.answer("Fan nomini kiriting..", reply_markup=buttom_orqa)
    await state.set_state(FanForm.name)

@admin_router.message(FanForm.name)
async def fanNomBot(message:Message, state:FSMContext):
    AddFan(name=message.text)
    await message.answer("Muaffaqiyatli qo'shildi", reply_markup=Buttom_admin)
    await state.clear()



@admin_router.message(F.text == "Savol qo'shish 💡")
async def savolBot(message:Message, state:FSMContext):
    bottom = ReplyKeyboardBuilder()
    for i in readFanler():
        bottom.button(text=f"{i[1]}")
    bottom.button(text="Orqaga 🔙")
    bottom.adjust(2)
    await message.answer("Qaysi fanga qo'shmoqchisiz", reply_markup=bottom.as_markup(resize_keyboard=True, one_time_keyboard=True))
    await state.set_state(SavolForm.savol)

@admin_router.message(SavolForm.savol)
async def savol1Bot(message:Message, state:FSMContext):
    xabar = message.text
    await state.update_data({'fan': xabar})
    await message.answer("Savol textini yuboring...")
    await state.set_state(SavolForm.a)

@admin_router.message(SavolForm.a)
async def savol2Bot(message:Message, state:FSMContext):
    xabar = message.text
    await state.update_data({"savol" : xabar})
    await message.answer("A javob uchun text yuboring...")  
    await state.set_state(SavolForm.b)

@admin_router.message(SavolForm.b)
async def savol3Bot(mesage:Message, state:FSMContext):
    xabar = mesage.text
    await state.update_data({'a':xabar})
    await mesage.answer("B javobi uchun text yuboring...")
    await state.set_state(SavolForm.c)

@admin_router.message(SavolForm.c)
async def savol4Bot(message:Message, state:FSMContext):
    xabar = message.text
    await state.update_data({"b": xabar})
    await message.answer("C javob uchun text yuboring...")
    await state.set_state(SavolForm.tj)

@admin_router.message(SavolForm.tj)
async def savol5Bot(messsage:Message, state:FSMContext):
    xabar = messsage.text
    await state.update_data({"c": xabar})
    data = await state.get_data()
    javoblar = InlineKeyboardBuilder()
    javoblar.button(text=data.get("a"), callback_data=data.get("a"))
    javoblar.button(text=data.get("b"), callback_data=data.get("b"))
    javoblar.button(text=data.get("c"), callback_data=data.get("c"))
    javoblar.adjust(1)
    await messsage.answer("To'gri javobni belgilang", reply_markup=javoblar.as_markup())
    await state.set_state(SavolForm.finish)

@admin_router.callback_query(SavolForm.finish)
async def Savol6Bot(call:CallbackQuery, state:FSMContext):
    xabar = call.data
    await state.update_data({"tj":xabar})
    data = await state.get_data()
    await call.message.answer(f"Fan: {data.get("fan")}\nSavol: {data.get("savol")}\nA javob: {data.get("a")}\nB javob: {data.get("b")}\nC javob: {data.get("c")}\nT'g'ri javob: {data.get("tj")}\n\nMalumotlar to'g'rimi ", reply_markup=Buttom_tekshir)
    await state.set_state(SavolForm.finish2)

@admin_router.callback_query(SavolForm.finish2)
async def savol7Bot(call:CallbackQuery, state:FSMContext):
    xabar = call.data
    if xabar == "ha":
        data = await state.get_data()
        AddSavol(fan=data.get('fan'), savol=data.get('savol'), a=data.get('a'), b=data.get('b'), c=data.get('c'), tj=data.get("tj"))
        await call.message.answer("Muaffaqiyatli bajarildi",reply_markup=Buttom_admin)
        await state.clear()
    else:
        await call.message.answer("Bekor qilindi" ,reply_markup=Buttom_admin)
        await state.clear()



@admin_router.message(F.text == "Fan o'chirish 🗑️")
async def fanDelBot(message:Message, state:FSMContext):
    fanlar = InlineKeyboardBuilder()
    for i in readFanler():
        fanlar.button(text=f"{i[1]}", callback_data=i[1])
    fanlar.button(text=f"Orqaga 🔙", callback_data="Orqaga 🔙")
    # fanlar = ReplyKeyboardBuilder()
    # for i in readFanler():
    #     fanlar.button(text=i[1])
    # fanlar.button(text="Orqaga 🔙")
    fanlar.adjust(2)
    await message.answer("Qaysi fani o'chirmoqchisiz", reply_markup=fanlar.as_markup())
    await state.set_state(Fandelete.fan)

@admin_router.callback_query(Fandelete.fan)
async def fanDel2Bot(cal:CallbackQuery, state:FSMContext):
    xabar = cal.data
    for i in readFanler():
        if str(i[1]) == str(xabar):
            await state.update_data({"fan": xabar})
            await cal.message.answer(f"Xaqiqatdan ham {xabar}ni o'chirmoqchimisiz", reply_markup=Buttom_tekshir)
            await state.set_state(Fandelete.finish)

@admin_router.callback_query(Fandelete.finish)
async def Fandel2Bot(cal:CallbackQuery, state:FSMContext):
    xabat = cal.data
    data = await state.get_data()
    if xabat == "ha":
        DeleteFan(name=data.get("fan"))
        await cal.message.answer("Muaffaqiyatli o'chirildi", reply_markup=Buttom_admin)
    else:
        await cal.message.answer("Amal bekor qilindi", reply_markup=Buttom_admin)
        await state.clear()




@admin_router.message(F.text == "Savol o'chirish 🚮")
async def savoldel(message:Message, state:FSMContext):
    fanlar = InlineKeyboardBuilder()
    for i in readFanler():
        fanlar.button(text=f"{i[1]}", callback_data=f"{i[1]}")
    fanlar.button(text="Orqaga 🔙", callback_data="Orqaga 🔙")
    fanlar.adjust(2)
    await message.answer("Qaysi fanga tegishli savolni o'chirmoqchisiz", reply_markup=fanlar.as_markup())
    await state.set_state(SavolDel.fan)

@admin_router.callback_query(SavolDel.fan)
async def savolDel1(cal:CallbackQuery, state:FSMContext):
    xabar = cal.data
    savol = InlineKeyboardBuilder()
    for i in readSavollar():
        if str(i[0]) == str(xabar):
            savol.button(text=f"{i[1]}",callback_data=i[1])
    savol.button(text="Orqaga 🔙", callback_data="Orqaga 🔙")
    savol.adjust(1)
    await cal.message.answer("Qaysi savolni o'chirmoqchisiz", reply_markup=savol.as_markup())
    await state.set_state(SavolDel.savol)

@admin_router.callback_query(SavolDel.savol)
async def savol3del(cal:CallbackQuery, state:FSMContext):
    xabar = cal.data
    await state.update_data({"savol":xabar})
    await cal.message.answer(f"Haqiqatdan ham {xabar} savolini o'chirmoqchimisiz? " ,reply_markup=Buttom_tekshir)
    await state.set_state(SavolDel.final)

@admin_router.callback_query(SavolDel.final)
async def savol3del(cal:CallbackQuery, state:FSMContext):
    xabar = cal.data
    data = await state.get_data()
    if xabar == "ha":
        print(data.get('savol'))
        DeleteSavol(name=data.get('savol'))
        await cal.message.answer("Muaffaqiyatli o'chirildi", reply_markup=Buttom_admin)
    else:
        await cal.message.answer("Bekor qilindi", reply_markup=Buttom_admin)

    await state.clear()


@admin_router.message(F.text == "User sifatida sinab ko'rish 🚀")
async def usBot(message:Message):
    await message.answer("User darajasiga o'tkazildi", reply_markup=Buttom_user_no)



@admin_router.message(F.text == "Taklif va shikoyatlarni ko'rish 👀")
async def shikbot(messagee:Message, state:FSMContext):
    shik = InlineKeyboardBuilder()
    for i in readShik():
        shik.button(text=f"{i[1]}",callback_data=f'{i[1]}')
    shik.button(text="Orqaga 🔙", callback_data="Orqaga 🔙")
    shik.adjust(1)
    await messagee.answer("Taklif va shikoyatlardan birini tanlang", reply_markup=shik.as_markup())
    await state.set_state(shikForm.shikoyat)

@admin_router.callback_query(shikForm.shikoyat)
async def shik2Bot(cal:CallbackQuery, state:FSMContext):
    xabar = cal.data
    for i in readShik():
        if i[1] == xabar:
            await state.update_data({"user_id" : i[0]})
    await cal.message.answer(f"Javobingizni yuboring ✍️", reply_markup=buttom_orqa)
    await state.set_state(shikForm.finish)

@admin_router.message(shikForm.finish)
async def shik3Bot(message:Message,state:FSMContext):
    await message.answer("Xabar yuborildi")
    xabar = message.text
    data = await state.get_data()
    await bot.send_message(chat_id=data.get('user_id'), text=f"{xabar}", reply_markup=Buttom_admin)
    deleteShik(user_id=data.get('user_id'))
    await state.clear()
    
    
        
