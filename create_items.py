from burger import Burger
from burger_combo import Burger_combo
from drink import Drink
from items import Items
from nugget import Nugget
from nugget_combo import Nugget_combo
from side import Side
from cart import Cart

class createItems:

    menu_dict={
        1:("Big Mac", 8.99, 1000),
        2:("Cheese Burger", 9.99, 1500),
        3:("Double Cheeseburger", 14.99, 2500),
        4:("3Pc Nugget", 2.99, 300),
        5:("10Pc Nugget", 2.99, 600),
        6:("20Pc Nugget", 3.99, 1200),
        7:("Sprite", 4.99, 500),
        8:("Coca-Cola", 4.99, 600),
        9:("Fanta", 4.99, 340),
        10:("Dr Pepper", 4.99, 320),
        11:("Fries", 2.99, 100),
        12:("Apple Slices", 3.99, 40),
        13:("Onion Rings", 4.99, 90),
        14:("Muffin", 6.99, 100),
        15:"B Combo",
        16:"N Combo"
        }

    def __init__(self, value1, value2 = 0, value3 = 0, value4 = 0):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4

    def createFood(self):
        if(0<self.value1<4):
            food_data = createItems.menu_dict[self.value1]
            userBurger = Burger(food_data[0],food_data[1], food_data[2])
            return userBurger
       
        if(3 < self.value1 < 7):
            food_data = createItems.menu_dict[self.value1]
            userNugget = Nugget(food_data[0],food_data[1], food_data[2])
            return userNugget

        if(6 < self.value1 < 11):
            food_data = createItems.menu_dict[self.value1]
            userDrink = Drink(food_data[0],food_data[1], food_data[2])
            return userDrink

        if(10 < self.value1 < 15):
            food_data = createItems.menu_dict[self.value1]
            userSide = Side(food_data[0],food_data[1], food_data[2])
            return userSide

        if(self.value1 == 15):

            food_data = createItems.menu_dict[self.value2]
            userBurger = Burger(food_data[0],food_data[1], food_data[2])

            food_data = createItems.menu_dict[self.value3]
            userDrink = Drink(food_data[0],food_data[1], food_data[2])

            food_data = createItems.menu_dict[self.value4]
            userSide = Side(food_data[0],food_data[1], food_data[2])

            bur_combo = Burger_combo(userDrink, userSide, userBurger, createItems.menu_dict[self.value1])
            return bur_combo

        if(self.value1 == 16):

            food_data = createItems.menu_dict[self.value2]
            userNugget = Nugget(food_data[0],food_data[1], food_data[2])

            food_data = createItems.menu_dict[self.value3]
            userDrink = Drink(food_data[0],food_data[1], food_data[2])

            food_data = createItems.menu_dict[self.value4]
            userSide = Side(food_data[0],food_data[1], food_data[2])

            nug_combo = Nugget_combo(userDrink, userSide, userNugget, createItems.menu_dict[self.value1])
            return nug_combo