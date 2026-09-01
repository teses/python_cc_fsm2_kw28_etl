
import traceback
from src.config import Config
from src.logger import Logger
from src.database import DatabaseEngine

from src.etl.ETL_VORLAGE import ETL_VORLAGE
from src.etl.ETL_VORLAGE_MULTIPLE import ETL_VORLAGE_MULTIPLE
from src.etl.ETLPricefile import ETLPricefile
from src.etl.ETLGpsr import ETLGpsr
from src.etl.ETLDLists import ETLDLists
from src.etl.ETLContentListsContent import ETLContentListsContent
from src.etl.ETLContentListsSpecifications import ETLContentListsSpecifications
from src.etl.ETLApplicationLists import ETLApplicationLists

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
    ETLDLists(config=config, logger=logger, engine=engine),
    ETLContentListsContent(config=config, logger=logger, engine=engine),
    ETLContentListsSpecifications(config=config, logger=logger, engine=engine),
    ETLApplicationLists(config=config, logger=logger, engine=engine),
]


for pipeline in pipelines:
    try:
        logger.info("-"*50)
        pipeline.run()

    except Exception as e:
        print(f"Fehler in {pipeline.__class__.__name__}: {e}")
        traceback.print_exc()


logger.info("fertig....")
