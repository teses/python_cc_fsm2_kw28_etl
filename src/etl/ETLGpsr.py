import pandas as pd
from src.etl.ETLSinglePipeline import ETLSinglePipeline


class ETLGpsr(ETLSinglePipeline):

    def _extract(self):

        file = self._config.config["other"]
        self._logger.info(f"Starte _extract() der Datei {file}")

        df = pd.read_csv(
            file,
            sep=";",
            encoding="utf-8",
            dtype = str
        )
        return df

    def _transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self._logger.info("Starte _transform()")

        # Doppelte ganze zeilen entfernen
        df = df.drop_duplicates()

        # nuller zeilen entfernen
        df = df.dropna(how="all")

        # Spaltennamen bereinigen
        df.columns = df.columns.str.strip()
        df.columns = df.columns.str.lower()
        df.columns = df.columns.str.replace(" ", "_")
        df.columns = df.columns.str.replace(".", "")
        df.columns = df.columns.str.replace("-", "")

        return df

    def _load(self, df: pd.DataFrame):

        self._logger.debug(f"start load into db table: {self._config.config['dbtables']['gpsr']}")

        rows_imported = df.to_sql(
            self._config.config['dbtables']['gpsr'],
            con=self._db_conn,
            if_exists="replace",  # replace , append
            index=False
        )

        self._logger.info(f"{rows_imported} rows imported to table {self._config.config['dbtables']['gpsr']}")

