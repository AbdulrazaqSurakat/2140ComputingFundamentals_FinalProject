from items import Items

class Burger(Items):# burger class is defined and inherits from "Items" parent class


    def __init__(self, name, cost, calories) -> None: # contructor and arguments inside init
        super().__init__(cost, calories)# gives asccess to methods and properties of Items parent class
        self.name = name# initializes name