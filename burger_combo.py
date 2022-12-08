from items import Items
from drink import Drink
from side import Side
from burger import Burger


SAVINGS = 0.9 #initialize savings amount

class Burger_combo(Items):
    """creates burger_combo class for burger combo option on menu
       contains constructor for burger combo class
    """

    def __init__(self, drink, side, burger, name) -> None:# contructor and arguments inside init
        """initializes the Burger_combo

        Args:
            hold info on burger combo order
        """
        calories = drink.calories + side.calories + burger.calories #initializes caroies as combination of all the food item calories
        cost = round(SAVINGS * (drink.cost + side.cost + burger.cost), 2)# rounds and initializes costs as combination of all the costs 
        super().__init__(cost, calories)# gives asccess to methods and properties of Items class
        self.drink = drink# initializes drink
        self.side = side# initializes side
        self.burger = burger# initializes burger
        self.name = name# initializes name