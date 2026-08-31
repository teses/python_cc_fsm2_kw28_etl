
import pandas as pd
from src.etl.ETLSinglePipeline import ETLSinglePipeline


class ETL_VORLAGE(ETLSinglePipeline):


    def _extract(self)  :
        self._logger.info("Starte _extract()")
        personen = [
            {"Name": "Max", "Alter": 25, "Stadt": "Berlin"},
            {"Name": "Anna", "Alter": 30, "Stadt": "Hamburg"},
            {"Name": "Tom", "Alter": 22, "Stadt": "Köln"}
        ]
        df = pd.DataFrame(personen)
        return df


    def _transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self._logger.info("Starte _transform()")
        df["Alter_2"] = df["Alter"] + 10
        #print(df)
        return df


    def _load(self, df: pd.DataFrame):
        self._logger.info("Starte _load()")
        print(df)
        count = df.to_sql(
            "personen",
            con=self._db_conn,
            if_exists="replace",  # replace , append
            index=False
        )
        self._logger.info(f"importiert: {count}")
