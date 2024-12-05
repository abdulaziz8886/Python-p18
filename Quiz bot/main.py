import logging
import asyncio
from aiogram import Bot, Dispatcher
from config import token
from users.user import user_router
from users.admin import admin_router

dp = Dispatcher()
bot = Bot(token=token)
logging.basicConfig(level=logging.INFO)


dp.include_router(user_router)
dp.include_router(admin_router)



async def main():
    await bot.send_message(chat_id=5678926023, text="Bot ishga tushdi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("tugadi")