from cart_view import Cart_view

class Menu_view:
    def __init__(self, cart):
        self.cart = Cart_view(cart)
        self.menu = {
        1:("Big Mac", 8.99, 1000),
        2:("Cheese", 9.99, 1500),
        3:("Double", 14.99, 2500),
        4:("3P Nug", 2.99, 300),
        5:("10P Nug", 2.99, 600),
        6:("20P Nug", 3.99, 1200),
        7:("Sprite", 4.99, 500),
        8:("Coke", 4.99, 600),
        9:("Fanta", 4.99, 340),
        10:("DPepper", 4.99, 320),
        11:("Fries", 2.99, 100),
        12:("Apples", 3.99, 40),
        13:("Onion", 4.99, 90),
        14:("Muffin", 6.99, 100),
        15:("B Combo", "tbd", "tbd"),
        16:("N Combo", "tbd", "tbd")
        }

    def displayMenu(self):
        print("Item #\t\tName\t\tCost($)\t\tCalories")
        print("-----------------------------------------------------------------------------------")
        for key in self.menu:
            print(key, end='\t\t')
            print(self.menu[key][0], end='\t\t')
            print(self.menu[key][1], end='\t\t')
            print(self.menu[key][2], end='\t\t\n')

    def get_item(self):
        userItem = input("Which item would you like today (enter item #): ")
        while not userItem.isdigit():
            print("Input must be an integer")
            userItem = input("Which item would you like today (enter item #): ")
        
        return int(userItem)

    def get_amount(self):
        userAmount = input("How many of this item would you like?: ")
        while not userAmount.isdigit():
            print("Input must be an integer")
            userAmount = input("How many of this item would you like?: ")
        return int(userAmount)    

    def get_burger(self):
        userBurger = input("Which burger do you want in the combo?: ")
        while not userBurger.isdigit():
            print("Input must be an integer")
            userBurger = input("Which burger do you want in the combo?: ")
        return int(userBurger)

    def get_nugget(self):
        userNugget = input("Which nugget do you want in the combo?: ")
        while not userNugget.isdigit():
            print("Input must be an integer")
            userNugget = input("Which nugget do you want in the combo?: ")
        return int(userNugget)

    def get_side(self):
        userSide = input("Which side do you want in the combo?: ")
        while not userSide.isdigit():
            print("Input must be an integer")
            userSide = input("Which side do you want in the combo?: ")
        return int(userSide)  

    def get_drink(self):
        userDrink = input("Which drink do you want in the combo?: ")
        while not userDrink.isdigit():
            print("Input must be an integer")
            userDrink = input("Which drink do you want in the combo?: ")
        return int(userDrink)              

    def display_invalid_item(self):
        print("That item number is not available from the item category/menu, try again")   

    def display_invalid_amount(self):
        print("Item amount invalid, please try again")    

    def get_continue(self):
        cont = input("Would you like to order another item (y/n)?: ")
        if cont == "y":
            return True

        elif cont == "n":
            return False         

