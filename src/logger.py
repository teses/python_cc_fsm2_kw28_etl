
import logging

class Logger:

    def __init__(self, logfile="", level=logging.DEBUG):

        # Die Handler festlegen
        handlers = [
            logging.StreamHandler()
        ]
        # wenn logfile leer, dann kein logging in Datei
        if(logfile !=""):
            handlers.append(logging.FileHandler(logfile, encoding="utf-8"))

        # logger Config
        logging.basicConfig(
            level = level,
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            handlers=handlers
        )

        # logger
        self.logger = logging.getLogger('etl')


    def debug(self, message):
        self.logger.debug(message)


    def info(self, message):
        self.logger.info(message)


    def warning(self, message):
        self.logger.warning(message)


    def error(self, message):
        self.logger.error(message)


    def critical(self, message):
        self.logger.critical(message)
