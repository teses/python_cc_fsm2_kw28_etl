
import pandas as pd
from src.etl.ETLMultiplePipeline import ETLMultiplePipeline
from sqlalchemy import text
from src.config import Config
from src.logger import Logger
from src.database import DatabaseEngine

class ETL_VORLAGE_MULTIPLE(ETLMultiplePipeline):


    def __init__(self, config: Config, logger: Logger, engine: DatabaseEngine):
        super().__init__(config, logger, engine)
        #self._logger.info(self._config.config['pricefile'])
        self._counts = 0


    def _before_run(self):
        self._logger.info("drop table personen_multiple ")
        # Tabelle löschen
        with self._db_conn.begin() as conn:
            conn.execute(text(f"DROP TABLE IF EXISTS personen_multiple "))


    def _extract(self)  :
        self._logger.info("Starte _extract()")

        data = [
            [
                {"Name": "Max", "Alter": 25, "Stadt": "Berlin"},
                {"Name": "Anna", "Alter": 30, "Stadt": "Hamburg"},
                {"Name": "Tom", "Alter": 22, "Stadt": "Köln"}
            ],
            [
                {"Name": "Helmut", "Alter": 25, "Stadt": "Berlin"},
                {"Name": "Tanja", "Alter": 30, "Stadt": "Hamburg"},
                {"Name": "Franz", "Alter": 22, "Stadt": "Köln"}
            ]
        ]

        for item in data :
            df = pd.DataFrame(item)
            yield df


    def _transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self._logger.info("Starte _transform()")
        df["Alter_2"] = df["Alter"] + 10
        #print(df)
        return df


    def _load(self, df: pd.DataFrame):
        self._logger.info("Starte _load()")
        #print(df)
        count = df.to_sql(
            "personen_multiple",
            con=self._db_conn,
            if_exists="append",  # replace , append
            index=False
        )
        self._counts += count
        self._logger.info(f"importiert: {count}")


    def _after_run(self):
        self._logger.info(f"menge aller importierten: {self._counts}")