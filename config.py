from os import getenv
import logging
import decimal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

decimals = decimal.Context()
decimals.prec = 8

class Config(object):
    # Config for in .env file
    TG_TOKEN = getenv("TG_TOKEN")
    QIWI_TOKEN = getenv("QIWI_TOKEN")
    DATABASE_URL = getenv("DATABASE_URL")
