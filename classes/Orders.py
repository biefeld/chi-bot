import json

class Orders:
    def __init__(self, path: str = './db/orders.json') -> None:
        self.path = path
        self.orders = self.load()

    def __str__(self) -> str:
        return str(self.orders)

    def load(self) -> dict:
        with open(self.path) as f:
            return json.load(f)

    def is_new_user(self, name: str) -> bool:
        return (self.get_next_order_id(name) == 1)

    def get_next_order_id(self, name: str) -> int:
        print(self.orders)
        print(self.orders.keys())
        return 1

    def get_dishes(self, course):
        pass
