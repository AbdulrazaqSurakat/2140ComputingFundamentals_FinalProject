from items import Items
from drink import Drink
from side import Side
from nugget import Nugget

SAVINGS = 0.9

class Nugget_combo(Items):
    def __init__(self, drink, side, nugget, name) -> None:
        calories = drink.calories + side.calories + nugget.calories
        cost = round(SAVINGS * (drink.cost + side.cost + nugget.cost), 2)
        super().__init__(cost, calories)
        self.drink = drink
        self.side = side
        self.nugget = nugget
        self.name = name