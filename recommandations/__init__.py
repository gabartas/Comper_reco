import datetime
import json
import os

from flask import Flask
from flask.logging import default_handler
from flask_cors import CORS

from .logger import initLogger


# ----------------------------
# Application Factory Function
# ----------------------------


def create_app():
    # Create the Flask application
    app = Flask(__name__)
    CORS(app)
    # Configure Recommandations default settings application
    app.config.from_file('../settings.json', load=json.load)

    # Configure the Flask application
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)
    app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(minutes=60)

    configure_logging(app)
    register_cli_commands(app)

    from recommandations.routes import api, initStrategies
    app.register_blueprint(api)
    initStrategies(app)

    return app

# ----------------
# Helper Functions
# ----------------


def configure_logging(app):
    # Remove the default logger configured by Flask
    app.logger.removeHandler(default_handler)

    # Logging Configuration
    if app.config['LOG_WITH_GUNICORN']:
        globallogger = initLogger(app.config["LOG_LEVEL"], True)
    else:
        globallogger = initLogger(app.config["LOG_LEVEL"], False)
        # app.logger.addHandler(globallogger.file_handler())
    app.logger.handlers.extend(globallogger.getHandlers())
    app.logger.info('Starting Comper Recommandations Service...')


def register_cli_commands(app):
    @app.cli.command('')
    def initialize():
        """Initialize """
