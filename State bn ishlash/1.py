import logging
from aiogram import Bot, Dispatcher, F
import asyncio
from aiogram.types import Message, CallbackQuery, FSInputFile
from config import token, Ovozbot
from aiogram.filters import CommandStart
from DefoltButton import menyu, til_almashtirish
from states import Form
from aiogram.fsm.context import FSMContext
from deep_translator import GoogleTranslator
import os






dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)


@dp.message(CommandStart())
async def BoshlashBot(message: Message, state: FSMContext):
    await message.answer("Assalomu alaykum Translate botga Xush kelibsiz", reply_markup=menyu)
    await state.set_state(Form.til)

@dp.message(Form.til)
async def TilTanlaBot(message: Message, state: FSMContext):
    xabar = message.text
    await state.update_data({'til':xabar})
    await message.answer("Tarjima qilmoqchi so'zingizni kiriting: ")
    await state.set_state(Form.soz)


@dp.message(Form.soz)
async def TarjimaJarayon(message: Message, state: FSMContext):
    xabar = message.text
    if xabar == "til almashtirish":
        await message.answer("Til tanlang: ", reply_markup=menyu)
        await state.set_state(Form.til)
    else:
        data = await state.get_data()
        til = data.get("til")
        tarjima = GoogleTranslator(source=f"{til[:2]}", target=f"{til[7:9]}").translate(f"{xabar}")
        Ovozbot(xabar=tarjima)
        voice = FSInputFile(path="voice.mp3")
        await message.reply_voice(voice=voice,caption=f"{tarjima}", reply_markup=til_almashtirish)
        os.remove("voice.mp3")




async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("tugadi")
