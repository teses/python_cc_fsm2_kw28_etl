
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError



class DatabaseEngine():

    def __init__(self, host, user, password, database, port=3306):
        self.connection = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}",
            echo=False  # debug ausgabe
        )

        try:
            with self.connection.connect() as conn:
                pass

        except SQLAlchemyError as e:
            raise ConnectionError(
                f"Datenbank nicht erreichbar: "
                f"{host}:{port}/{database}"
            ) from e

