from items import Items

class Nugget(Items):
    def __init__(self, name, cost, calories) -> None:# initializes the objects attributes
        super().__init__(cost, calories) #gives asccess to methods and attributes of Items parent class
        self.name = name# initializes name
        