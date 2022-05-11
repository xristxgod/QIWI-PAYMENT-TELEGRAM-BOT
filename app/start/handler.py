import random

from aiogram import types

from app.start.__init__ import *
from app.start import keyboards

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    logger.error("HANDLER: start")
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
    logger.error("HANDLER: bot_message")
    if message.chat.type == "private":
        if message.text.isdigit():
            message_money = decimals.create_decimal(message.text)
            if message_money >= 5:
                comment = str(message.from_user.id) + "_" + str(random.randint(1000, 9999))
                bill = p2p.bill(amount=message_money, lifetime=15, comment=comment)

            else:
                await bot.send_message(message.from_user.id, "Min sum for top up is 5 RUB")
        else:
            await bot.send_message(message.from_user.id, "Say float or integer number:")

@dp.callback_query_handlers(text="top_up")
async def top_up(callback_query: types.CallbackQuery):
    logger.error("CALLBACK: top_up")
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, "Say sum for top up: ")

