from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btnTopUp = InlineKeyboardButton(text="Top up balance", callback_data="top_up")
topUpMenu = InlineKeyboardMarkup(row_width=1)
topUpMenu.insert(btnTopUp)