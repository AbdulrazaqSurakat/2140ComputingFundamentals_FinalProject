from burger import Burger
from burger_combo import Burger_combo
from drink import Drink
from items import Items
from nugget import Nugget
from nugget_combo import Nugget_combo
from side import Side

class Create_items:
    """this class is meant to create the food item based on one or multiple inputs
    """

    #this dictionary holds values of all of the served items, includes name, price and calories in the value
    #key is the item number
    menu_dict={
        1:("Big Mac", 8.99, 1000),
        2:("Cheese", 9.99, 1500),
        3:("Cheese", 14.99, 2500),
        4:("3Pc Nug", 2.99, 300),
        5:("10Pc Nug", 2.99, 600),
        6:("20Pc Nug", 3.99, 1200),
        7:("Sprite", 4.99, 500),
        8:("Coke", 4.99, 600),
        9:("Fanta", 4.99, 340),
        10:("DPepper", 4.99, 320),
        11:("Fries", 2.99, 100),
        12:("Apple", 3.99, 40),
        13:("Onion", 4.99, 90),
        14:("Muffin", 6.99, 100),
        15:"B Combo",
        16:"N Combo"
        }

    def __init__(self, value1, value2 = 0, value3 = 0, value4 = 0):
        """initializes the create_item object

        Args:
            value1 (int): the item the user wants to order, if this is 15 or 16 then values are needed for the 3 other values to make the combo
            value2 (int, optional): the burger or the nugget the user wants to order for a combo. Defaults to 0.
            value3 (int, optional): the drink the user wants to get with their combo. Defaults to 0.
            value4 (int, optional): the side the user wants to get with their combo. Defaults to 0.
        """
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4

    def createFood(self):
        """create the food item object that was ordered by the user

        Returns:
            item: the item that the user orders
        """
        #creates a burger if ordered
        if(0<self.value1<4):
            food_data = Create_items.menu_dict[self.value1]
            userBurger = Burger(food_data[0],food_data[1], food_data[2])
            return userBurger

        #creates a nugget if ordered
        if(3 < self.value1 < 7):
            food_data = Create_items.menu_dict[self.value1]
            userNugget = Nugget(food_data[0],food_data[1], food_data[2])
            return userNugget

        #creates a drink if ordered
        if(6 < self.value1 < 11):
            food_data = Create_items.menu_dict[self.value1]
            userDrink = Drink(food_data[0],food_data[1], food_data[2])
            return userDrink

        #creates a side if ordered
        if(10 < self.value1 < 15):
            food_data = Create_items.menu_dict[self.value1]
            userSide = Side(food_data[0],food_data[1], food_data[2])
            return userSide

        #creates a burger combo if ordered
        if(self.value1 == 15):

            #creates necessary burger
            food_data = Create_items.menu_dict[self.value2]
            userBurger = Burger(food_data[0],food_data[1], food_data[2])

            #creates necessary drink
            food_data = Create_items.menu_dict[self.value3]
            userDrink = Drink(food_data[0],food_data[1], food_data[2])

            #creates necessary side
            food_data = Create_items.menu_dict[self.value4]
            userSide = Side(food_data[0],food_data[1], food_data[2])

            #creates the combo that was ordered
            bur_combo = Burger_combo(userDrink, userSide, userBurger, Create_items.menu_dict[self.value1])
            return bur_combo

        #creates a nugget combo if ordered
        if(self.value1 == 16):

            #creates necessary nugget
            food_data = Create_items.menu_dict[self.value2]
            userNugget = Nugget(food_data[0],food_data[1], food_data[2])

            #creates necessary drink
            food_data = Create_items.menu_dict[self.value3]
            userDrink = Drink(food_data[0],food_data[1], food_data[2])

            #creates necessary side
            food_data = Create_items.menu_dict[self.value4]
            userSide = Side(food_data[0],food_data[1], food_data[2])

            #creates the nugget combo oitem with all of the above created items
            nug_combo = Nugget_combo(userDrink, userSide, userNugget, Create_items.menu_dict[self.value1])
            return nug_combo