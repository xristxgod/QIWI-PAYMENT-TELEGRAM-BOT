from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from pyqiwip2p import QiwiP2P

from src.__init__ import DB, cnf_tg, cnf_qiwi

bot = Bot(token=cnf_tg.get, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

p2p = QiwiP2P(auth_key=cnf_qiwi.get)
db = DB

# <<<============================================>>> Run bot <<<=====================================================>>>

def run():
    # Run bot
    executor.start_polling(dp, skip_updates=True)