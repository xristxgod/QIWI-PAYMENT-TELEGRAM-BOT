from aiogram import types

from app.start.__init__ import *
from app.start import keyboards

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if message.chat.type == "private":
        if not (await db.user_exists(message.from_user.id)):
            await db.add_user(message.from_user.id, "@" + message.from_user.username)
        await bot.send_message(
            message.from_user.id, (
                f"Welcome!\n"
                f"Your balance: {db.get_user_balance(message.from_user.id)} RUB"
            ),
            reply_markup=keyboards.topUpMenu
        )

@dp.message_handler()
async def bot_message(message: types.Message):
    pass

@dp.callback_query_handlers(text="top_up")
async def top_up(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, "Say sum for top up: ")

