from aiogram import Bot, Dispatcher
from aiogram import types

from src.__init__ import DB
from config import Config

bot = Bot(token=Config.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
db = DB