
from abc import ABC, abstractmethod
import pandas as pd
from src.config import Config
from src.logger import Logger
from src.database import DatabaseEngine


class ETLPipeline(ABC):

    def __init__(
            self,
            config: Config,
            logger: Logger,
            engine: DatabaseEngine
    ):
        self._config = config
        self._logger = logger
        self._db_conn = engine.connection

    @abstractmethod
    def _extract(self) -> pd.DataFrame:
        pass


    @abstractmethod
    def _transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass


    @abstractmethod
    def _load(self, df: pd.DataFrame):
        pass

    @abstractmethod
    def run(self):
        pass


    def _before_run(self):
        self._logger.info("Starte ETL Pipeline")


    def _after_run(self):
        self._logger.info("ETL beendet")







