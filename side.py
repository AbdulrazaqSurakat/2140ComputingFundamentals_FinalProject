from items import Items

class Side(Items):
    """creates Side class for Side option on menu
       contains constructor for Side class
    """

    def __init__(self, name, cost, calories) -> None:# initializes the objects attributes
        """initializes the Side class

        Args:
            holds the info on side that user ordered
        """
        super().__init__(cost, calories)#inheritance, #gives asccess to methods and attributes of Items parent class
        self.name = name# initializes name