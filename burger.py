from items import Items

class Burger(Items):# burger class is defined and inherits from "Items" parent class
    """creates burger class forburger option on menu
       contains constructor for burger class
    """


    def __init__(self, name, cost, calories) -> None: # contructor and arguments inside init
        """initializes the Burger class

        Args:
            holds the info on burger that user ordered
        """
        super().__init__(cost, calories)# gives asccess to methods and properties of Items parent class
        self.name = name# initializes name