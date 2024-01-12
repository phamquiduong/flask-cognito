from flask import Flask
from werkzeug.exceptions import HTTPException

from core.config import Config, config


def create_app(config_class=Config):
    # Create Flask application
    app = Flask(__name__)

    # Configure Flask
    app.config.from_object(config_class)
    config.set_class(config_class)

    # Custom exception handler
    from core.errors.handle_exception import exception_handler, http_exception_handler
    app.register_error_handler(HTTPException, http_exception_handler)
    app.register_error_handler(Exception, exception_handler)

    # Register Flask blueprint
    from apps.auth.routes import auth_route
    app.register_blueprint(auth_route, url_prefix='/auth')

    return app


def handler(event, context):
    app = create_app()

    from flask_cors import CORS
    CORS(app)

    from core.logger import logger
    logger.info('Event: %s', event)
    logger.info('Context: %s', context)

    import awsgi
    return awsgi.response(app, event, context)
