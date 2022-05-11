from aiogram import Bot, Dispatcher
from aiogram import types

from config import Config

bot = Bot(token=Config.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)