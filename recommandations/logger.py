import logging
from logging.handlers import RotatingFileHandler


loggering = None


def initLogger(level, gunicorn):
    global loggering
    loggering = Logger(level, gunicorn)
    return loggering


class Logger():
    def __init__(self, level, gunicorn):
        self.level = level
        if gunicorn:
            self.logr = logging.getLogger('gunicorn.error')
            self.logr.setLevel(self.level)
            self.logr.info("Gunicorn Logger initialisation")
        else:
            formatter = logging.Formatter(
                '%(asctime)s | [%(levelname)s]: %(message)s')
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            self.logr = logging.getLogger("stdout")
            self.logr.addHandler(handler)
            self.logr.setLevel(self.level)
            self.logr.info("StdOut Logger initialisation")

    def getLogger(self):
        return self.logr

    def getHandlers(self):
        return self.logr.handlers

    def file_handler(self):
        file_handler = RotatingFileHandler('../logs/reco.log',
                                           maxBytes=16384,
                                           backupCount=20)
        file_formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(threadName)s-%(thread)d: %(message)s [in %(filename)s:%(lineno)d]')
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(self.level)
        return file_handler
