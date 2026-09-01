
from abc import ABC, abstractmethod
import pandas as pd
from src.config import Config
from src.logger import Logger
from src.database import DatabaseEngine
from sqlalchemy import text

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

    def _setIndexOnTableColumn(self, table_name, column_name):

        sql = f"ALTER TABLE {table_name} ADD INDEX index_{table_name}_{column_name} ({column_name});"
        self._logger.debug(sql)

        with self._db_conn.connect() as conn:
            conn.execute(text(sql))
            conn.commit()

    def _before_run(self):
        self._logger.info(f"Starte ETL Pipeline: {self.__class__.__name__}")


    def _after_run(self):
        self._logger.info(f"ETL beendet: {self.__class__.__name__}")







