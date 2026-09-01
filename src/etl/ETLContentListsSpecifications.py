import pandas as pd
from src.etl.ETLMultiplePipeline import ETLMultiplePipeline
from sqlalchemy.types import Integer, String, Float, DateTime
from sqlalchemy import text
from src.config import Config
from src.logger import Logger
from src.database import DatabaseEngine
from os import listdir
from os.path import isfile, join


class ETLContentListsSpecifications(ETLMultiplePipeline):

    def __init__(self, config: Config, logger: Logger, engine: DatabaseEngine):
        super().__init__(config, logger, engine)
        self._counts = 0


    def _before_run(self):
        self._drop_table(self._config.config['dbtables']['specifications'])


    def _extract(self) -> pd.DataFrame:
        data_files = [
            f for f in listdir(self._config.config["contentlists"])
            if isfile(join(self._config.config["contentlists"], f)) and f[-10:] == "DE_v3.xlsx"
        ]

        self._logger.info(f"{len(data_files)} Dateien werden gelesen")
        iter = 1
        for data_file in data_files:
            self._logger.info(f"{iter}/{len(data_files)}. extract {data_file} ")

            excel_file = join(self._config.config["contentlists"], data_file)

            data = pd.read_excel(
                excel_file,
                dtype=str,
                sheet_name="specifications"
            )
            iter += 1
            yield data


    def _transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df.columns = df.columns.str.replace(" - ", "_")
        # Spaltennamen bereinigen
        df.columns = df.columns.str.strip()
        df.columns = df.columns.str.lower()
        return df

    def _load(self, df: pd.DataFrame):
        self._logger.debug(f"start load into db table: {self._config.config['dbtables']['specifications']}")

        rows_imported = df.to_sql(
            name=self._config.config['dbtables']['specifications'],
            con=self._db_conn,
            if_exists="append",  # replace , append
            index=False,
            dtype={
                "itemnumber": String(50)
            }
        )
        self._counts += rows_imported
        self._logger.info(f"{rows_imported} rows imported to table {self._config.config['dbtables']['specifications']}")

    def _after_run(self):
        self._logger.info(f"menge aller importierten: {self._counts}")

