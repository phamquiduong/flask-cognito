import awsgi
from flask import Flask
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from core.config import Config
from core.errors.handle_exception import http_exception_handler
from core.logger import logger


def create_app(config_class=Config):
    logger.info('Creating app')
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Custom exception handler
    app.register_error_handler(HTTPException, http_exception_handler)

    # Register Flask blueprint
    logger.info('Register authenticate blueprint')
    from apps.auth.routes import auth_route
    app.register_blueprint(auth_route, url_prefix='/auth')

    logger.info('Create app success %s', app)
    return app


def handler(event, context):
    logger.info('Event: %s', event)
    logger.info('Context: %s', context)

    logger.info('Start create app')
    app = create_app()

    logger.info('Config CORS for app')
    CORS(app)

    logger.info('Start awsgi server')
    return awsgi.response(app, event, context)
