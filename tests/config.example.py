from pathlib import Path


class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent

    SECRET_KEY = ''

    DEBUG = False
    TESTING = True
    IS_RUN_ON_LAMBDA = False

    AWS_ACCESS_KEY_ID = ''
    AWS_SECRET_ACCESS_KEY = ''

    AWS_REGION = ''
    USER_POOL_ID = ''
    CLIENT_ID = ''
