from aiogram import types, F, Router

menu_router = Router()


@menu_router.callback_query(F.data=="menu")
async def menu_handler(callback: types.CallbackQuery):
    replykb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Pizza"),
                types.KeyboardButton(text="Cheese")
            ]
        ]
    )
    await callback.message.answer(text="Вот наше меню" ,reply_markup=replykb)

