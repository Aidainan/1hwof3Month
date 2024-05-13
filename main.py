import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from handlers.start import start_router
from handlers.pic import pic_router
from handlers.myinfo import myinfo_router
from handlers.echo import echo_router
from handlers.menu import menu_router
from dotenv import load_dotenv
from os import getenv
import logging

import random
from pathlib import Path
load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


async def main():
    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(myinfo_router)
    dp.include_router(echo_router)
    dp.include_router(menu_router)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

