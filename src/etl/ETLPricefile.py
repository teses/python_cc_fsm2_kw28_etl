
import pandas as pd
from jupyter_core.migrate import regex
from sqlalchemy.types import Integer, String, Float, DateTime
from src.etl.ETLSinglePipeline import ETLSinglePipeline


class ETLPricefile(ETLSinglePipeline):


    def _extract(self)  :

        file = self._config.config["pricefile"]
        self._logger.info(f"Starte _extract() der Datei {file}")

        df = pd.read_csv(
            file,
            sep="\t",
            encoding="utf-8",
            dtype={
                "EUHarmonizedCode" : str,
                "UnNumber" : str,
                "UnNumber" : str,
                "EANBarcode" : str,
            }
        )
        self._logger.info(f"{df.shape[0]} Zeilen eingelesen")
        #print(df["EANBarcode"].isna().sum())
        #print(df.info())
        #print(df.describe())

        return df


    def _transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self._logger.info("Starte _transform()")

        # Doppelte ganze zeilen entfernen
        df = df.drop_duplicates()

        # Bruttopreis anhand des Nettos
        df["DealerPriceBrutto"] = round(df["DealerPrice"] * (1 + (self._config.config['vat'] / 100)), 2)

        # das + wegnehmen und datentyp richtig machen
        df["Availability"] = df["Availability"].str.replace("+", "")
        df["Availability"] = df["Availability"].astype(int)
        df["USAvailability"] = df["USAvailability"].str.replace("+", "")
        df["USAvailability"] = df["USAvailability"].astype(int)

        # die Zahlen bei den Produktgruppen entfernen
        df["ProductGroup"] = df["ProductGroup"].str.replace(r"^\d+-", "", regex=True)
        df["ProductType"] = df["ProductType"].str.replace(r"^\d+-", "", regex=True)

        # Spaltennamen bereinigen
        df.columns = df.columns.str.strip()
        df.columns = df.columns.str.lower()

        # menge der ungültigen
        ungueltig2 = df[df["itemnumber"].isna() | (df["itemnumber"] == "") ]
        self._logger.info(f"ungültige Daten: {ungueltig2.shape[0]}")

        #print(df.info())
        #print(df.describe())
        return df


    def _load(self, df: pd.DataFrame):
        self._logger.debug(f"start load into db table: {self._config.config['dbtables']['pricefile']}")

        rows_imported = df.to_sql(
            self._config.config['dbtables']['pricefile'],
            con=self._db_conn,
            if_exists="replace",  # replace , append
            index=False,
            dtype = {
                "itemnumber": String(50)
            }
        )

        self._logger.info(f"{rows_imported} rows imported to table {self._config.config['dbtables']['pricefile']}")


    def _after_run(self):
        self._setIndexOnTableColumn(
            table_name=self._config.config['dbtables']['pricefile'],
            column_name = "itemnumber"
        )
        self._logger.info(f"ETL beendet: {self.__class__.__name__}")

