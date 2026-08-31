

from src.etl.ETLPipeline import ETLPipeline

class ETLSinglePipeline(ETLPipeline):

    def run(self):
        self._before_run()

        d = self._extract()
        d = self._transform(d)
        self._load(d)

        self._after_run()