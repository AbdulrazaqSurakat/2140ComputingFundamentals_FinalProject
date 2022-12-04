from items import Items

class Nugget(Items):
    def __init__(self, name, cost, calories) -> None:
        super().__init__(cost, calories)
        self.name = name
        