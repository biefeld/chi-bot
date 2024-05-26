import json
import os


class Menu:
    def __init__(self, path: str = './db/menu.json') -> None:
        self.path = path
        self.menu = self.load()

    def __str__(self) -> str:
        return str(self.menu)

    def load(self):
        if (not os.path.isdir('./db')):
            os.mkdir('./db')
            return {}

        with open(self.path) as f:
            return json.load(f)

    def get_courses(self):
        pass

    def get_dishes(self, course):
        pass
