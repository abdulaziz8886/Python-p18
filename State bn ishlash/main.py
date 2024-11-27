from aiogram import Bot, Dispatcher, F
import asyncio
import logging
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message, FSInputFile
from config import token, stat
from buttoms import menyu, tekshir1
from aiogram.fsm.context import FSMContext  

bp = Dispatcher()
logging.basicConfig(level=logging.INFO)
bot = Bot(token = token)



@bp.message(CommandStart())
async def StartBot(message:Message, state:FSMContext):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}\nKim izlayapsiz 🔎", reply_markup=menyu)
    await state.set_state(stat.hodim)

@bp.message(stat.hodim)
async def hodim(message:Message, state: FSMContext):
    await message.answer("""Sherik topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await message.answer("Ism, familiyangizni kiriting?")
    await state.set_state(stat.texnalogiya)
    await state.update_data({"nachun": message.text})


@bp.message(stat.texnalogiya)
async def texBot(message:Message, state:FSMContext):
    # ism = list(message.text.split())
    # if len(ism) != 2:
    #     data = await state.get_data()
    #     data.pop("nachun", None)  
    #     await state.update_data(data)
    #     await state.set_state(stat.hodim)
    #     await message.answer("qaytdi")
    await state.update_data({"Ismi": message.text})
    await message.answer("""📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#""")
    await state.set_state(stat.Aloqa)


@bp.message(stat.Aloqa)
async def aloqaBot(message:Message, state:FSMContext):
    await state.update_data({"texnalogiya": message.text,
                            "username" : message.from_user.username})
    await message.answer("""📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67""")
    await state.set_state(stat.hudud)


@bp.message(stat.hudud)
async def hududBot(message:Message, state:FSMContext):
    await state.update_data({"aloqa": message.text})
    await message.answer("""🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await state.set_state(stat.narxi)

@bp.message(stat.narxi)
async def NarxiBot(message:Message, state:FSMContext):
    await state.update_data({"hudud": message.text})
    await message.answer("""💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?""")

    await state.set_state(stat.murojat)


@bp.message(stat.murojat)
async def murojatBot(message:Message, state:FSMContext):
    await state.update_data({'narxi': message.text})
    await message.answer("""🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00""")
    await state.set_state(stat.maqsad)

@bp.message(stat.maqsad)
async def maqsadBot(message:Message, state:FSMContext):
    await state.update_data({"Murojat": message.text})
    data = await state.get_data()
    if data.get('nachun') == "Sherik kerak":
        nachun = f"🏅{data.get('nachun').split()[0]}"
    elif data.get('nachun') == "Ish joyi kerak":
        nachun = "🧑🏼 Hodim"
    elif data.get('nachun') == "Ustoz kerak":
        nachun = "🎓 Shogird"
    else:
        nachun = "🎓 Ustoz"
    await message.answer(f"{data.get('nachun')}:\n\n{nachun}: {data.get("Ismi")}\n📚 Texnologiya: {data.get("texnalogiya")}\n🇺🇿 Telegram: @{data.get("username")}\n📞 Aloqa: {data.get("aloqa")}\n🌐 Hudud: {data.get("hudud")}\n💰 Narxi : {data.get("narxi")}\n🕰 Murojaat qilish vaqti: {data.get("Murojat")}\n\n\n👆Ushbu malumotlar to'g'rimi?👆", reply_markup=tekshir1)
    await state.set_state(stat.tekshir)


@bp.callback_query(stat.tekshir)
async def tekshir(cal:CallbackQuery, state:FSMContext):
    if cal.data == "ha":
        data = await state.get_data()
        if data.get('nachun') == "Sherik kerak":
            nachun = f"🏅{data.get('nachun').split()[0]}"
        elif data.get('nachun') == "Ish joyi kerak":
            nachun = "🧑🏼 Hodim"
        elif data.get('nachun') == "Ustoz kerak":
            nachun = "🎓 Shogird"
        else:
            nachun = "🎓 Ustoz"
        await bot.send_message(chat_id = 5678926023, text=f"{data.get('nachun')}:\n\n{nachun}: {data.get("Ismi")}\n📚 Texnologiya: {data.get("texnalogiya")}\n🇺🇿 Telegram: @{data.get("username")}\n📞 Aloqa: {data.get("aloqa")}\n🌐 Hudud: {data.get("hudud")}\n💰 Narxi : {data.get("narxi")}\n🕰 Murojaat qilish vaqti: {data.get("Murojat")}\n\n\n👆Ushbu malumotlar to'g'rimi?👆", reply_markup=tekshir1)
        await cal.message("Sizning arizaning 24 soat ichida ko'rib chiqiladi")
    else:
        data = await state.get_data()
        data.clear()
    






async def main():
    await bp.start_polling(bot)
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("tugadi")