import json
import os

DIR = './db'

class Menu:
    def __init__(self) -> None:
        self.path = f'{DIR}/menu.json'
        self.menu = self.load()

    def __str__(self) -> str:
        return str(self.menu)

    def load(self):
        if (not os.path.isdir(DIR)):
            os.mkdir(DIR)
            return {}

        with open(self.path) as f:
            return json.load(f)

    def get_courses(self):
        pass

    def get_dishes(self, course):
        pass
