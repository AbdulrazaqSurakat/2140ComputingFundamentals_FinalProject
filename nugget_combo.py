from items import Items
from drink import Drink
from side import Side
from nugget import Nugget

SAVINGS = 0.9# initializes savings on nuggest_combo 

class Nugget_combo(Items):
    """creates Nuggest_combo class for nugget combo option on menu
       contains constructor for nugget combo class
    """

    def __init__(self, drink, side, nugget, name) -> None:# initializes the objects attributes
        """initializes the Nugget_combo class

        Args:
            holds the info on Nugget_combo that user ordered
        """
        calories = drink.calories + side.calories + nugget.calories# initializes calories with savings already calculated
        cost = round(SAVINGS * (drink.cost + side.cost + nugget.cost), 2)# initializes cost with savings already calculated
        super().__init__(cost, calories)#gives asccess to methods and attributes of Items parent class
        self.drink = drink# initializes drink
        self.side = side# initializes side
        self.nugget = nugget# initializes nuggets
        self.name = name# initializes name