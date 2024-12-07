from aiogram import Router, F
from aiogram.types import Message, ChatPermissions
from filters.group import GroupFilter
from aiogram.filters import and_f
from datetime import datetime, timedelta
import asyncio

group_router = Router()

# Guruhga kirdi chiqdilarni filtirlash uchun biz quydagicha codelardan foydalana

@group_router.message(GroupFilter(), F.text == "Bot")
async def get_new_chat(message: Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}\nNima yordam bera olaman")

@group_router.message(GroupFilter(), F.text)
async def totiBot(message:Message):
    await message.answer(f"{message.text}")









