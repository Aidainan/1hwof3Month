import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging

import random
from pathlib import Path
load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}")


@dp.message(Command("pic"))
async def send_pic(message: types.Message):
    file_name = random.choice(list((Path(__file__).parent/"Images").iterdir()))
    file_path = Path(__file__).parent.parent / "Images" / file_name
    logging.info(file_path)
    file = types.FSInputFile(file_path)
    await message.answer_photo(file)


@dp.message(Command("myinfo"))
async def myinfo(message: types.Message):
    logging.info(message.from_user)
    await message.answer(
        f"Ваш Id:, {message.from_user.id},"
        f"\n" f"Ваше Имя:, {message.from_user.first_name},"
        f"\n" f"Ваш никнейм: {message.from_user.username}\n")



@dp.message()
async def echo(message: types.Message):
    await message.answer("Привет")
    await message.answer(message.text)


async def main():
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

