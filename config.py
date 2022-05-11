from os import environ
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config(object):
    TOKEN = environ.get("TOKEN")