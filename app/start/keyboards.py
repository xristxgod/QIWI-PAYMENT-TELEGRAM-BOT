from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

topUpMenu = InlineKeyboardMarkup(row_width=1)
btnTopUp = InlineKeyboardButton(text="Top up balance", callback_data="top_up")
topUpMenu.insert(btnTopUp)

def buy_menu(is_url: bool = True, url: str = None, bill: str = None):
    qiwiMenu = InlineKeyboardMarkup(row_width=1)
    if is_url:
        btnUrlQIWI = InlineKeyboardButton(text="Link to payment", url=url)
        qiwiMenu.insert(btnUrlQIWI)
    btnCheckQIWI = InlineKeyboardButton(text="Check payment", callback_data=f"check_{bill}")
    qiwiMenu.insert(btnCheckQIWI)
    return qiwiMenu