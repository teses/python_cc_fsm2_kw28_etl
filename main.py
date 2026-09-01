
from src.config import Config
from src.logger import Logger
from src.database import DatabaseEngine

from src.etl.ETL_VORLAGE import ETL_VORLAGE
from src.etl.ETL_VORLAGE_MULTIPLE import ETL_VORLAGE_MULTIPLE
from src.etl.ETLPricefile import ETLPricefile
from src.etl.ETLGpsr import ETLGpsr


# get config
config = Config("config.json")



# logger initialisieren
logger = Logger(
    logfile = config.config['logging']['file'],
    level   = config.config['logging']['level']
)

# get db connection
engine = DatabaseEngine(
    database = config.config['db']['database'],
    host     = config.config['db']['host'],
    user     = config.config['db']['user'],
    password = config.config['db']['password']
)


pipelines = [
    ETLPricefile(config=config, logger=logger, engine=engine),
    ETLGpsr(config=config, logger=logger, engine=engine),
]


for pipeline in pipelines:
    try:
        pipeline.run()
    except Exception as e:
        print(f"Fehler in {pipeline.__class__.__name__}: {e}")
