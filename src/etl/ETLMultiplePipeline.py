

from src.etl.ETLPipeline import ETLPipeline

class ETLMultiplePipeline(ETLPipeline):

    def run(self):

        self._before_run()

        for d in self._extract():
            d = self._transform(d)
            self._load(d)

        self._after_run()