from aiogram import Bot, Dispatcher
from aiogram import types

from pyqiwip2p import QiwiP2P

from src.__init__ import DB
from config import Config

bot = Bot(token=Config.TG_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

p2p = QiwiP2P(auth_key=Config.QIWI_TOKEN)
db = DB
