import awsgi
from flask import Flask
from flask_cors import CORS

from core.config import Config
from core.logger import logger


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Flask extension
    CORS(app)

    # Flask blueprint
    from apps.auth.routes import auth_route
    app.register_blueprint(auth_route, url_prefix='/auth')

    return app


def handler(event, context):
    logger.info('Event: %s', event)
    logger.info('Context: %s', context)
    app = create_app()
    return awsgi.response(app, event, context)
