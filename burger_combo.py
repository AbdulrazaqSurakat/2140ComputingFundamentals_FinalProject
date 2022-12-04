from items import Items
from drink import Drink
from side import Side
from burger import Burger


SAVINGS = 0.9

class Burger_combo(Items):
    def __init__(self, drink, side, burger, name) -> None:
        calories = drink.calories + side.calories + burger.calories
        cost = round(SAVINGS * (drink.cost + side.cost + burger.cost), 2)
        super().__init__(cost, calories)
        self.drink = drink
        self.side = side
        self.burger = burger
        self.name = name