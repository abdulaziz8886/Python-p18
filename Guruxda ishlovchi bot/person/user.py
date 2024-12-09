from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from filters.users import UserPrivateFilter
from filters.group import ChenelSub
from config.config import chenel_id, token
bot = Bot(token=token)

user_router = Router()

kanal = {
    "1-kanal" : "https://t.me/learn_python_3_5",
    "2-kanal" : "https://t.me/empty_none_1"
}

tugma = InlineKeyboardBuilder()
for i in kanal:
    tugma.button(text=f"{i}", url=f"{kanal[f'{i}']}")
tugma.button(text = "Tekshirish ✅", callback_data="tekshir")
tugma.adjust(1)

@user_router.message(CommandStart())
async def checksub(message:Message) -> None:
    await message.answer("👇 Pastdagi kanallarga obuna bo'ling", reply_markup=tugma.as_markup())

@user_router.callback_query(F.data == "tekshir")
async def tekBot(cal:CallbackQuery):
    user_status = await bot.get_chat_member(chenel_id[0], cal.from_user.id)
    if user_status.status == "left":
        await cal.message.answer(f"1-kanalga obuna bo'lmadingiz", reply_markup=tugma.as_markup())
    else:
        user_status2 = await bot.get_chat_member(chenel_id[1], cal.from_user.id)
        if user_status2.status == "left":
            await cal.message.answer(f"2-kanalga obuna bo'lmadingiz", reply_markup=tugma.as_markup())
        else:
            await cal.message.answer("Obuna bo'ldingiz")
            await cal.message.answer("Echo botdan foydalanishiningiz mumkin")



@user_router.message(UserPrivateFilter(), F.text)
async def BotStart(message: Message):
    user_status = await bot.get_chat_member(chenel_id[0], message.from_user.id)
    if user_status.status == "left":
        await message.answer(f"1-kanalga obuna bo'lmadingiz", reply_markup=tugma.as_markup())
    else:
        user_status2 = await bot.get_chat_member(chenel_id[1], message.from_user.id)
        if user_status2.status == "left":
            await message.answer(f"2-kanalga obuna bo'lmadingiz", reply_markup=tugma.as_markup())
        else:
            await message.send_copy(chat_id=message.from_user.id)



