from items import Items

class Nugget(Items):
    """creates Nugget class for Nugget option on menu
       contains constructor for Nugget class
    """
        
    def __init__(self, name, cost, calories) -> None:# initializes the objects attributes
        """initializes the Nugget class

        Args:
            holds the info on Nugget that user ordered
        """
        super().__init__(cost, calories) #gives asccess to methods and attributes of Items parent class
        self.name = name# initializes name
        