from items import Items

class Drink(Items):

    def __init__(self, name, cost, calories, size) -> None:
        super().__init__(cost, calories)
        self.size = size
        self.name = name