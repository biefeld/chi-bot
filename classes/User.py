class User:
    def __init__(self, name: str = None) -> None:
        self.name = name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_greeting(self) -> str:
        return f'Welcome {self.name}, I hope your doing well'