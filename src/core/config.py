import os
from pathlib import Path


class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent

    SECRET_KEY = os.environ['SECRET_KEY']

    DEBUG = os.getenv('DEBUG', 'true').lower() == 'true'
    TESTING = os.getenv('TESTING', 'true').lower() == 'true'

    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
    LOG_DIR = BASE_DIR / '../log'
    LOG_HANDLER = os.getenv('LOG_HANDLER', '').split(',')

    AWS_REGION = os.environ['AWS_REGION']
    USER_POOL_ID = os.environ['USER_POOL_ID']
    CLIENT_ID = os.environ['CLIENT_ID']
