import os


# Determine the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    # Logging
    LOG_WITH_GUNICORN = os.getenv('LOG_WITH_GUNICORN')


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    LOG_WITH_GUNICORN = True


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    LOG_WITH_GUNICORN = False


class TestingConfig(Config):
    TESTING = True
    LOG_WITH_GUNICORN = False
    WTF_CSRF_ENABLED = False
