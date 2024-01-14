import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

# Load environment variables
if not load_dotenv():
    raise FileNotFoundError('Environment variable not found')


class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent

    SECRET_KEY = os.getenv('SECRET_KEY', '')

    DEBUG = os.getenv('DEBUG', 'true').lower() == 'true'
    TESTING = os.getenv('TESTING', 'true').lower() == 'true'

    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
    LOG_DIR = BASE_DIR / '../log'
    LOG_HANDLER = os.getenv('LOG_HANDLER', '').split(',')

    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')

    IS_RUN_ON_LAMBDA = os.getenv('IS_RUN_ON_LAMBDA', None) is not None

    AWS_REGION = os.getenv('AWS_REGION', '')
    USER_POOL_ID = os.getenv('USER_POOL_ID', '')
    CLIENT_ID = os.getenv('CLIENT_ID', '')


class ConfigClass:
    def __init__(self):
        self.__config_class = None

    def set_class(self, config_class):
        self.__config_class = config_class

    def get(self, key: str, default: Any = None):
        return getattr(self.__config_class, key) if default is None else getattr(self.__config_class, key, default)


config = ConfigClass()
