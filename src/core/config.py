import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    DEBUG = os.getenv('DEBUG', 'true').lower() == 'true'
    TESTING = os.getenv('TESTING', 'true').lower() == 'true'
    SECRET_KEY = os.environ['SECRET_KEY']
