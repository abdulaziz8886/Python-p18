from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
token = "7795399235:AAEG8EE355KFICKTbgKa4zwU-LCW5TkFSOc"
bot = Bot(token=token)
import asyncio
from CRUD import *
from butoms import *
from state import *


admins = [5678926023]
oson_parol = ["12345678","87654321", "11111111", "22222222", "33333333", "44444444", "55555555", "66666666", "77777777", "88888888", "99999999", "00000000", "01234567"]
user_router = Router()

@user_router.message(CommandStart())
async def startBot(message:Message):
    if message.from_user.id in admins:
        await message.answer(f"Assalomu Alaykum {message.from_user.full_name}\nSizga adminlik huquqi berilgan", reply_markup=Buttom_admin)
    else:
        user_id = str(message.from_user.id)
        users = readlogin()  # Ro'yxatni bir marta yuklab oling
        await message.answer(f"{message.from_user.id}")
        # Foydalanuvchini ro'yxatda qidirish
        for i in users:
            if user_id == str(i[2]):
                if i[-1].lower() == "y":
                    await message.answer(f"Assalomu Alaykum {message.from_user.full_name}", reply_markup=Buttom_user_yes)
                else:
                    await message.answer(f"Assalomu Alaykum {message.from_user.full_name}", reply_markup=Buttom_user_no)
                return
            
        await message.answer("☹️ Afsuski, sizda akkaunt mavjud emas.'Ro'yxatdan o'tish ✍️' tugmasi orqali akkaunt yaratishingiz mumkin.",reply_markup=Buttom_user_no)


@user_router.message(F.text == "Orqaga 🔙")
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


@user_router.callback_query(F.data == "Orqaga 🔙")
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

@user_router.message(F.text == "Parolim esimda yoq 😢")
async def parolBot(message:Message, state:FSMContext):
    await message.answer("Parol almashtirish faollashdi")
    await message.answer("Shaxsiy parolingizni almashtirish uchun shaxsinizni tasdiqlang")
    await message.answer("Telfon raqam kiriting 📞", reply_markup=cantoct)
    await state.set_state(parol_almash.parol1)




@user_router.message(parol_almash.parol1)
async def parolBot(mesage:Message, state:FSMContext):
    if mesage.contact.user_id == mesage.from_user.id:
        await mesage.answer("Yangi parolni kiriting 🆕")
        await state.set_state(parol_almash.parol2)
    else:
        await mesage.reply(f"😠 Iltimos saxsiy cantact bering")

@user_router.message(parol_almash.parol2)
async def parol2bot(message:Message, state:FSMContext):
    user_id = message.from_user.id
    xabar = message.text
    if len(xabar) >= 6:
        updateParol(login=xabar, user_id=user_id)
        await message.answer("Maffaqiyatli bajarildidi ✅", reply_markup=buttom_orqa)
        await state.clear()
    else:
        await message.answer("Kuchsiz parol qaytadan urinib ko'ring 🫣", reply_markup=cantoct)
        await state.clear()



@user_router.message(F.text == "Parolim yodimda yoq 😢")
async def ParBot(message:Message, state:FSMContext):
    await message.answer("Parol almashtirish faollashdi")
    await message.answer("Shaxsiy parolingizni almashtirish uchun shaxsinizni tasdiqlang")
    await message.answer("Telfon raqam kiriting 📞", reply_markup=cantoct)
    await state.set_state(parol_almash2.parol1)

cnt2 = []
@user_router.message(parol_almash2.parol1)
async def Par2bot(mesage:Message, state:FSMContext):
    data = await state.get_data()
    tel = mesage.contact.phone_number
    for i in readlogin():
        if str(i[4]) == str(data.get('ism')):
            if f"+{i[3]}" == str(tel):
                if mesage.contact.user_id == mesage.from_user.id:
                    await mesage.answer("Yangi parolni kiriting 🆕")
                    await state.set_state(parol_almash2.parol2)
                else:
                    await mesage.reply(f"😠 Iltimos saxsiy cantact bering")
            else:
                await mesage.answer("Joriy accauntga boshqa telfon raqam ulangan !")
                await mesage.answer("Bosh sahifaga qaytildi", reply_markup=Buttom_user_no)
                await state.clear()


@user_router.message(parol_almash2.parol2)
async def Par3Bot(message:Message, state:FSMContext):
    data = await state.get_data()
    xabar = message.text
    if str(xabar) in str(oson_parol):
        await message.answer(f"🫣 Oson parol kiritildi\nBoshqa parol o'ylab toping", reply_markup=buttom_orqa)
    else:
        if len(xabar) >= 6:
            await state.update_data({"parol1": xabar})
            updateParol(login=data.get('ism'), password=xabar)
            await message.answer("Parol muafaaqiyatli saqlandi ✅" ,reply_markup=Buttom_user_no)
            await state.clear()
        else:
            await message.answer("Ushbu parol yaroqsiz 👎", reply_markup=buttom_orqa)









@user_router.message(F.text == "Kirish ➡️")
async def KirishBot(message:Message, state:FSMContext):
    await message.answer("Loginingizni kiriting ✍️", reply_markup=buttom_orqa)
    await state.set_state(kirish_form.login)

@user_router.message(kirish_form.login)
async def kirBot(messsage:Message, state:FSMContext):
    xabar = messsage.text
    await state.update_data({"ism":xabar})
    for i in readlogin():
        if xabar == i[4]:
            await messsage.answer("Parolni kiriting 🔑", reply_markup=parol_almashtir_1)
            await state.set_state(kirish_form.parol)
            return
    await messsage.answer("Bunday login mavjud emas 🤷🏻‍♂️")

@user_router.message(kirish_form.parol)
async def parBot(message:Message, state:FSMContext):
    xabar = message.text
    data = await state.get_data()
    for i in readlogin():
        if str(i[4]) == str(data.get('ism')):
            if str(xabar) == str(i[5]):
                
                await message.answer("Accauntingiz tayyorlanmiqda 🛠️")
                await asyncio.sleep(2)
                await message.answer("Accauntingizda foydalanishingiz mumkin 😊", reply_markup=Buttom_user_yes)
                updateLog(log="y", user_id=message.from_user.id)
                await state.clear()
                return
            await message.answer("No to'g'ri parol ❌") 
            break           



@user_router.message(F.text == "Ro'yxatdan o'tish ✍")
async def KirishBot(message:Message, state:FSMContext):
    await message.answer("""📋 Shaxsiy kabinet uchun login o'ylab toping
❗️ 7 ta harkdan ko'p bo'lsin""" ,reply_markup=buttom_orqa)
    await state.set_state(user_form.login)

@user_router.message(user_form.login)
async def loginBot(message:Message, state:FSMContext):
    xabar = message.text
    for i in readlogin():
        if str(xabar) != str(i[4]):
            await state.update_data({"login": xabar})
            await message.answer(f"🔑 Parol o'ylab toping\n❌ 6 sondan kam bo'lmasin", reply_markup=buttom_orqa)
            await state.set_state(user_form.parol)
            return   
    await message.answer(f"🙅‍♂️ Joriy login band\nBoshqa login kiriting" ,reply_markup=buttom_orqa)

@user_router.message(user_form.parol)
async def parolBot(message:Message, state:FSMContext):
    xabar = message.text
    if str(xabar) in str(oson_parol):
        await message.answer(f"🫣 Oson parol kiritildi\nBoshqa parol o'ylab toping", reply_markup=buttom_orqa)
    else:
        if len(xabar) >= 6:
            await state.update_data({"parol1": xabar})
            await message.answer("Parolni takrorlang 🔄" ,reply_markup=buttom_orqa)
            await state.set_state(user_form.parol2)
        else:
            await message.answer("Ushbu parol yaroqsiz 👎", reply_markup=buttom_orqa)

@user_router.message(user_form.parol2)
async def parol2Bot(message:Message, state:FSMContext):
    xabar = message.text
    data = await state.get_data()
    parol1 = data.get("parol1")
    print(parol1)
    if parol1 == xabar:
        await message.answer("Telfon raqam kiriting 📞", reply_markup=cantoct or buttom_orqa)
        await state.set_state(user_form.tell)
    else:
        await message.answer("2 xil parol kiritildi, Qaytadan urunib ko'ring")

@user_router.message(user_form.tell, F.contact)
async def ContactBots(message: Message, state:FSMContext):
    xabar = message.contact.phone_number
    if message.contact.user_id == message.from_user.id:
        await state.update_data({"tel":xabar})
        data = await state.get_data()
        await message.answer(f"📝 Login: {data.get("login")}\n🔑 Parol: {data.get('parol1')}\n📞Tel : {xabar}\n Yuqoridagi malumotlar to'g'rimi", reply_markup=Buttom_tekshir)
        await state.set_state(user_form.finish)
    else:
        await message.reply(f"Siz boshqa telefon nomeringiz saqlandi")

@user_router.callback_query(user_form.finish)
async def finishBot(cal:CallbackQuery, state:FSMContext):
    data = await state.get_data()
    if cal.data == 'ha':
        addlogin(name=cal.from_user.full_name, user_name=f"@{cal.from_user.username}",user_id=cal.from_user.id,phone=data.get("tel"), login=data.get("login"), password=data.get("parol1"), log="y")
        await cal.message.answer("Muvaffaqiyatli ro'yxatdan o'tkazildi", reply_markup=Buttom_user_no)
    else:
        await cal.message.answer("Bosh saxifaga o'tildi" ,reply_markup=Buttom_user_no)



@user_router.message(F.text == "Ushbu bot nima qila oladi 🤔")
async def KirishBot(message:Message):
    await message.answer("🙋🏻‍♂️Assalomu Alaykim xurmatli foydalanuvchi ushbu bot ❓ Quiz bot xisoblanib kar bir o'zuvchi uchun shaxsiy 🔐 login, parollarini saqlagan xolda kirish-chiqishni nazorat qiladi va 👨🏻‍💻 adminga har bir o'quvchini ko'rsatayotgan 📈 natijalarini chiqarib boradi! 🚀")


@user_router.message(F.text == "👨‍💻 Dasturchi bn boglanish ☎️")
async def KirishBot(message:Message):
    await message.answer("""👨‍💻 Dasturchi bn boglanish ☎️
                         

👨🏻‍💼 Ism familiya: Ilhomboyev Abdulaziz
🎓 Tamomladi: DATA Talim stansiyasi
🌐 Telegram: @abdulaziz8886
🌐 Instagram https://www.instagram.com/abdu.laziz8886/""", reply_markup=Buttom_user_no)

@user_router.message(F.text == "👨‍💻 Dasturchi bn bog'lanish ☎️")
async def KirishBot(message:Message):
    await message.answer("""👨‍💻 Dasturchi bn boglanish ☎️
                         

👨🏻‍💼 Ism familiya: Ilhomboyev Abdulaziz
🎓 Tamomladi: DATA Talim stansiyasi
🌐 Telegram: @abdulaziz8886
🌐 Instagram https://www.instagram.com/abdu.laziz8886/""", reply_markup=Buttom_user_yes)






@user_router.message(F.text == "Test ishlash 🎓")
async def test1Bot(message:Message, state:FSMContext):
    fanlar = InlineKeyboardBuilder()
    for i in readFanler():
        fanlar.button(text=f"{i[1]}", callback_data=i[1])
    fanlar.button(text="Orqaga 🔙", callback_data="Orqaga 🔙")
    fanlar.adjust()
    await message.answer("Fan Tanlang 🔎", reply_markup=fanlar.as_markup())
    await state.set_state(TestIshla.fan)

cnt1 = []
savol_soni = 0
tj_soni = 0


@user_router.callback_query(TestIshla.fan)
async def test2bot(cal:CallbackQuery, state:FSMContext):
    xabar = cal.data
    global savol_soni, tj_soni
    savol_soni = 0
    tj_soni = 0
    savollar = InlineKeyboardBuilder()
    cnt = 1
    if cnt1 == []:
        for i in readSavollar():
            if str(i[0]) == str(xabar):
                cnt1.append(i[-1])
                savol_soni += 1
    for i in cnt1:
        for j in readSavollar():
            if j[-1] == i:
                await state.update_data({"id": i})
                savollar.button(text=j[2], callback_data=j[2])
                savollar.button(text=j[3], callback_data=j[3])
                savollar.button(text=j[4], callback_data=j[4])
                savollar.adjust(1)
                cnt1.remove(i)
                await cal.message.answer(f"{cnt} savol:\n{j[1]}", reply_markup=savollar.as_markup())
                break
        break
    await state.set_state(TestIshla.savol)

a = 0
b = 0
c = []
@user_router.callback_query(F.data == "keyingi savol ▶️")
async def tek2Bot(cal:CallbackQuery, state:FSMContext):
    savollar = InlineKeyboardBuilder()
    global savol_soni, tj_soni, a, b
    cnt = 2
    if cnt1 == []:
        await cal.message.answer("Testlar tugadi 🏁")
        foiz = (tj_soni / savol_soni) * 100
        if foiz > 80.0:
            await cal.message.answer_sticker(sticker="CAACAgIAAxkBAAKXomdQhenR38UBuR2WYAvjRrCBDrHNAAJNAAMkcWIaP0h_gyO63p02BA")
            await cal.message.answer(f"🥳Tabriklaymiz siz 80 % dan yoqori natijani qayd etdingiz 🎉\nJami savollar soni: {savol_soni}\nTo'gri javoblar soni: {tj_soni}\nFoiz: {foiz} %" ,reply_markup=Buttom_user_yes)
        elif foiz < 20.0:
            await cal.message.answer_sticker(sticker="CAACAgIAAxkBAAKXpGdQhnU61enl3Ee9LWP3Z2g8OOg2AAJPAAMkcWIaWMzn4qdTlUg2BA")
            await cal.message.answer(f"🙁 Afsiski siz 20 % dan past natijani qayd etdingiz 👎\nJami savollar soni: {savol_soni}\nTo'gri javoblar soni: {tj_soni}\nFoiz: {foiz} %", reply_markup=Buttom_user_yes)
        else:
            await cal.message.answer(f"Jami savollar soni: {savol_soni}\nTo'gri javoblar soni: {tj_soni}\nFoiz: {foiz} %", reply_markup=Buttom_user_yes)
        for i in readusers():
            c.append(i[2])
        if cal.from_user.id in c:
            a = i[3] + savol_soni
            b = i[4] + tj_soni
            updateUser(a=a, b=b, teach=(b / a) * 100, id2=cal.from_user.id)
        else:
            adduser(name=cal.from_user.full_name, User_name=cal.from_user.username,user_id=cal.from_user.id, savol_soni=savol_soni, javob_soni=tj_soni, teach=foiz)
  
    for i in cnt1:
        for j in readSavollar():
            if j[-1] == i:
                await state.update_data({"id": i})
                savollar.button(text=j[2], callback_data=j[2])
                savollar.button(text=j[3], callback_data=j[3])
                savollar.button(text=j[4], callback_data=j[4])
                savollar.adjust(1)
                cnt1.remove(i)
                await cal.message.answer(f"{cnt} savol:\n{j[1]}", reply_markup=savollar.as_markup())
                cnt+=1
                break
        break
    await state.set_state(TestIshla.savol)            


@user_router.message(cntForm.first)
async def cnt(message:Message, state:FSMContext):
    data = await state.get_data()




            
@user_router.callback_query(TestIshla.savol)
async def text4bot(cal:CallbackQuery, state:FSMContext):
    data = await state.get_data()
    global tj_soni
    xabar = cal.data
    for i in readSavollar():
        if i[-1] == data.get("id"):
            if str(i[-2]) == str(xabar):
                await cal.message.answer("To'g'ri 👍", reply_markup=fan_tekshir)
                tj_soni += 1
            else:
                await cal.message.answer("Xato 👎",reply_markup=fan_tekshir)
        


@user_router.message(F.text == "Shaxsiy statistikani ko'rish 👀")
async def korbot(message:Message):
    for i in readusers():
        if int(i[2]) == int(message.from_user.id):
            await message.answer(f"""Jami savollar soni: {i[3]}
To'gri javoblar soni: {i[4]}
Foiz: {i[5]} %""")




@user_router.message(F.text == "Login o'zgartirish 🛠️")
async def login1Bot(message:Message, state:FSMContext):
    await message.answer("Shaxsiy parolingizni kiriting ✍")
    await state.set_state(login_almash.login1)

@user_router.message(login_almash.login1)
async def login2Bot(message:Message, state:FSMContext):
    xabar = message.text
    user_id = message.from_user.id
    for i in readlogin():
        if str(i[2]) == str(user_id):
            if i[5] == xabar:
                await message.answer("Yangi loginingizni kiriting ✍")
                await state.set_state(login_almash.login2)
                return
    await message.answer("Notogri parol 🙅‍♂️")

@user_router.message(login_almash.login2)
async def login3Bot(message:Message, state:FSMContext):
    user_id= message.from_user.id    
    updateLogin(login=message.text, user_id=user_id)
    await message.answer("Maffaqiyatli bajarildi 👍", reply_markup=buttom_orqa)
    await state.clear()




@user_router.message(F.text == "Parolni almashtirish ⚙️")
async def login1Bot(message:Message, state:FSMContext):
    await message.answer("Parol almashtirish faollashdi")
    await message.answer("Shaxsiy parolingizni almashtirish uchun shaxsinizni tasdiqlang")
    await message.answer("Telfon raqam kiriting 📞", reply_markup=cantoct)
    await state.set_state(parol_almash.parol1)

@user_router.message(parol_almash.parol1)
async def parolBot(mesage:Message, state:FSMContext):
    xabar = mesage.contact.phone_number
    if mesage.contact.user_id == mesage.from_user.id:
        await mesage.answer("Yangi parolni kiriting")
        await state.set_state(parol_almash.parol2)
    else:
        await mesage.reply(f"Iltimos saxsiy cantact bering 🙅🏻‍♀️")

@user_router.message(parol_almash.parol2)
async def parol2bot(message:Message, state:FSMContext):
    user_id = message.from_user.id
    xabar = message.text
    if len(xabar) >= 6:
        updateParol(login=xabar, user_id=user_id)
        await message.answer("Maffaqiyatli bajarildidi 🎉", reply_markup=buttom_orqa)
        await state.clear()
    else:
        await message.answer("Kuchsiz parol qaytadan urinib ko'ring 🫣", reply_markup=cantoct)
        await state.clear()



@user_router.message(F.text == "Taklif yoki shikoyat qilish")
async def login1Bot(message:Message, state:FSMContext):
    await message.answer("Taklif yoki shikoyatingizni yozib qoldiring ✍️.")
    await state.set_state(taklifForm.taklif)

@user_router.message(taklifForm.taklif)
async def shikoyatBot(message:Message, state:FSMContext):
    await message.answer("Taklif yoki shikoyatingizni 24 soat ichida ko'rib chiqiladi ⏳", reply_markup=Buttom_user_yes)
    AddShikoyat(user_id=message.from_user.id, shik=f"{message.text}")
    await state.clear()



@user_router.message(F.text == "Chiqish 🔙")
async def chiqishBot(message:Message, state:FSMContext):
    await state.clear()
    await message.answer("Haqiqatdan ham chiqmoqchimisiz", reply_markup=Buttom_tekshir)
    await state.set_state(chiqishForm.chiqish)

@user_router.callback_query(chiqishForm.chiqish)
async def chiqBot(call:CallbackQuery):
    user_id = call.from_user.id
    if call.data == "ha":
        updateLog(log="n", user_id=user_id)
        await call.message.answer("Muaffaqiyatli chiqildi", reply_markup=Buttom_user_no)
    else:
        await call.message.answer("Bosh saxifaga qaytdingiz", reply_markup=Buttom_user_yes)