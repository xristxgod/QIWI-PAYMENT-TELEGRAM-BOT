from os import environ
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config(object):
    # Config for in .env file
    TG_TOKEN = environ.get("TG_TOKEN")
    QIWI_TOKEN = environ.get("TG_TOKEN")
    DATABASE_URL = environ.get("DATABASE_URL")