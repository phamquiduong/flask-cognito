import logging
from logging.config import dictConfig

from core.config import Config

if 'file' in Config.LOG_HANDLER:
    Config.LOG_DIR.mkdir(parents=True, exist_ok=True)

dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': Config.LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': Config.LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': Config.LOG_DIR / 'root.log',
            'maxBytes': 50000,
            'backupCount': 5,
        },

    },
    'root': {
        'handlers': Config.LOG_HANDLER,
        'level': Config.LOG_LEVEL,
        'propagate': True,
    }
})

logger = logging.getLogger()
