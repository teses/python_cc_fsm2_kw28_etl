


from src.config import Config
from src.logger import Logger
from src.database import DatabaseEngine
# from src.etl.ETLPricefile import ETLPricefile
from src.etl.ETL_VORLAGE import ETL_VORLAGE
from src.etl.ETL_VORLAGE_MULTIPLE import ETL_VORLAGE_MULTIPLE

#config = Config("config.json")
#
# print(config.config)
# print(config.config['pricefile'])
# print(config.config['db'])
# print(config.config['db']['host'])


#
# logger = Logger(logfile="logs/etl_pipeline.log", level="DEBUG")
# #logger = Logger(logfile="", level="DEBUG")
# logger.debug("Hallo ich bin eine debug meldung")
# logger.info("CSV-Datei wird eingelesen")
# logger.warning("Datensatz ohne Preis gefunden")
# logger.error("Fehler beim Schreiben in die Datenbank")
# logger.info("ETL-Prozess erfolgreich beendet")
# logger.critical("Absoluter Abbruch")

# import logging
#
# print(logging.INFO)
#
# t = getattr(logging, "INFO")
# print(t)


#engine = DatabaseEngine(database="comcave_etl", host="127.0.0.1", user="root", password="")
#print(engine.connection)

###########################################

config = Config("config.json")
logger = Logger(logfile="logs/etl_pipeline.log", level="DEBUG")
engine = DatabaseEngine(database="comcave_etl", host="127.0.0.1", user="root", password="")

#pipeline = ETL_VORLAGE(config=config, logger=logger, engine=engine)
pipeline = ETL_VORLAGE_MULTIPLE(config=config, logger=logger, engine=engine)
pipeline.run()





