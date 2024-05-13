from aiogram import types, Router
from aiogram.filters import Command
import logging

from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Ватсапп", url="https://t.me"),
            ],
            [
                types.InlineKeyboardButton(text="Меню", callback_data="menu")
            ]
        ]
    )
    logging.info(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}", reply_markup=kb)
