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
            amount = decimals.create_decimal(message.text)
            if amount >= 5:
                comment = str(message.from_user.id) + "_" + str(random.randint(1000, 9999))
                bill = p2p.bill(amount=amount, lifetime=15, comment=comment)
                await db.add_check(message.from_user.id, amount=amount, bill_id=bill.bill_id)
                await bot.send_message(message.from_user.id, (
                    f"You need to send {amount} RUB for our QIWI account\n"
                    f"Link to payment: {bill.pay_url} \n"
                    f"By specifying the payment comment: {comment}"
                ), reply_markup=keyboards.buy_menu(url=bill.pay_url, bill=bill.bill_id))
            else:
                await bot.send_message(message.from_user.id, "Min sum for top up is 5 RUB")
        else:
            await bot.send_message(message.from_user.id, "Say float or integer number:")

@dp.callback_query_handlers(text="top_up")
async def top_up(callback_query: types.CallbackQuery):
    logger.error("CALLBACK: top_up")
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, "Say sum for top up: ")

@dp.callback_query_handler(text_contains="check_")
async def check(callback_query: types.CallbackQuery):
    bill = str(callback_query.data[6:])
    info = await db.get_check(bill_id=bill, user_id=callback_query.from_user.id)
    if info:
        if str(p2p.check(bill_id=bill).status) == "PAID":
            user_balance = await db.get_user_balance(callback_query.from_user.id)
            amount = int(info[2])
            await db.set_user_balance(callback_query.from_user.id, balance=user_balance+amount)
            await bot.send_message(callback_query.from_user.id, "Your bill is top up!")
            await db.update_check(user_id=callback_query.from_user.id, bill_id=bill, status=True)
        else:
            await bot.send_message(
                callback_query.from_user.id,
                "You haven't paid the bill!",
                reply_markup=keyboards.buy_menu(False, bill=bill)
            )
    else:
        await bot.send_message(callback_query.from_user.id, "Bill is not found")