from items import Items

class Side(Items):
    def __init__(self, name, cost, calories) -> None:
        super().__init__(cost, calories)
        self.name = name