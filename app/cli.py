import sys
import argparse

from src.__init__ import cnf_tg, cnf_qiwi
from config import logger

def run_bot():
    from app.__init__ import run
    run()

def main():
    try:
        parser = argparse.ArgumentParser(prog="telegram_bot")
        parser.add_argument("-tt", "--tokenTG", default=None)
        parser.add_argument("-tq", "--tokenQIWI", default=None)
        args = parser.parse_args(sys.argv[1:])
        logger.error("--> SET CONFIG")
        cnf_tg.set(args.tokenTG)
        cnf_qiwi.set(args.tokenQIWI)
        logger.error("--> START BOT\n")
        run_bot()
    except Exception as error:
        logger.error(f"\nERROR: {error}\n")
    finally:
        logger.error("\n--> DEL CONFIG")
        cnf_tg.delete()
        cnf_qiwi.delete()