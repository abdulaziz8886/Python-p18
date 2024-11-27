from aiogram import Bot, Dispatcher, F
import asyncio
import logging
from config import token
from aiogram.filters.command import CommandStart
from aiogram.types import Message, CallbackQuery
from inlinebuuttons import menyu, Taomlar_menyu, Taomlar, Soni


dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)


@dp.message(CommandStart())
async def StartBot(message: Message):
    await message.answer_photo(photo="https://vsudu-sport.ru/wp-content/uploads/2018/12/zhirnyj-fastfud-i-vysokokalorijnye-sousy.jpg", caption=f"Assalomu alaykum {message.from_user.full_name}", reply_markup=menyu)

@dp.callback_query(F.data == "taom")
async def TaomlarBot(call: CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=638b4b371fc8631ebc72fba28ac80e50_l-6961938-images-thumbs&n=13", reply_markup=Taomlar_menyu.as_markup())
    await call.message.delete()

@dp.callback_query(F.data == "ortga 1")
async def OrtgaBot1(call: CallbackQuery):
    await call.message.answer_photo(photo="https://vsudu-sport.ru/wp-content/uploads/2018/12/zhirnyj-fastfud-i-vysokokalorijnye-sousy.jpg", caption=f"Bosh sahifaga qaytdingiz {call.from_user.full_name}", reply_markup=menyu)
    await call.message.delete()

@dp.callback_query(F.data)
async def TaomlarBuyurtma(call: CallbackQuery):
    xabar = call.data
    if xabar.isdigit():
        await call.answer(f"{xabar} zakaz berdingiz", show_alert=True)
        await call.message.delete()
        await call.message.answer_photo(photo="https://vsudu-sport.ru/wp-content/uploads/2018/12/zhirnyj-fastfud-i-vysokokalorijnye-sousy.jpg", caption=f"Bosh sahifaga qaytdingiz {call.from_user.full_name}", reply_markup=menyu)
    else:
        for i in Taomlar:
            if i == xabar:
                await call.message.answer_photo(photo=Taomlar[xabar][1], caption=f"Taom: {xabar}\nNarxi: {Taomlar[xabar][0]} so'm", reply_markup=Soni.as_markup())
                await call.message.delete()




async def main():
    await dp.start_polling(bot)
    
    
    
if name == 'main':
    try:
        asyncio.run(main())
    except:
        print("Tugadi")