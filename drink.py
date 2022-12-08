from items import Items

class Drink(Items):# drinks class is defined and inherits from "Items" parent class
    """creates drink class for drink option on menu
       contains constructor for drink class
    """
    def __init__(self, name, cost, calories) -> None:# contructor and arguments inside init
        """initializes the Drink class

        Args:
            holds the drink info that user ordered
        """
        super().__init__(cost, calories) #gives asccess to methods and properties of Items parent class
        self.name = name# initializes name