from aiogram import Bot, Dispatcher
import asyncio
import logging
from config import config
from person import user
from gurux import inpection

dp = Dispatcher()
bot = Bot(token=config.token)
logging.basicConfig(level=logging.INFO)


dp.include_router(user.user_router)
dp.include_router(inpection.group_router)


async def main():
    await bot.send_message(chat_id=5678926023, text="Bot ishga tushdi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("tugadi")