from aiogram import types, Router
import random
from pathlib import Path
from aiogram.filters import Command
import logging


pic_router = Router()


@pic_router.message(Command("pic"))
async def send_pic(message: types.Message):
    file_name = random.choice(list((Path(__file__).parent.parent /"Images").iterdir()))
    file_path = Path(__file__).parent.parent / "Images" / file_name
    logging.info(file_path)
    file = types.FSInputFile(file_path)
    await message.answer_photo(file)