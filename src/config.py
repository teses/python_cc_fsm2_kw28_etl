

import json

class Config:


    def __init__(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            self.config = json.load(file)


