from aiogram import types, F, Router

menu_router = Router()

@menu_router.callback_query(F.data == "menu")
async def menu_handler(callback: types.CallbackQuery):
    replykb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Pizza", callback_data="pizza"),
                types.InlineKeyboardButton(text="Cheese", callback_data="cheese")
            ]
        ]
    )
    await callback.message.answer("Вот наше меню", reply_markup=replykb)

@menu_router.callback_query(F.data == 'pizza')
async def pizza_handler(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Пицца 30см", callback_data="pizza_30"),
                types.InlineKeyboardButton(text="Пицца 40см", callback_data="pizza_40")
            ]
        ]
    )
    await callback.message.answer('Вот пиццы которые мы предлагаем', reply_markup=kb)

@menu_router.callback_query(F.data == 'cheese')
async def cheese_handler(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Сыр Маргарита", callback_data="cheese_margarita"),
                types.InlineKeyboardButton(text="Сыр Филадельфия", callback_data="cheese_philadelphia")
            ]
        ]
    )
    await callback.message.answer('Вот сыры которые мы предлагаем', reply_markup=kb)