from cart import Cart
from menu_view import Menu_view
from create_items import Create_items

class Controller:
    def __init__(self, model: Cart, view: Menu_view):
        self.model = model
        self.view = view

    def run_menu(self):
        while True:

            self.view.displayMenu()
            userItem = self.view.get_item()

            while (not (0 < userItem < 17)):
                self.view.display_invalid_item()
                userItem = self.view.get_item()

            if (0 < userItem < 15):
                new_item = Create_items(userItem)
                item = new_item.createFood()
            elif (15 == userItem):
                userBurger = self.view.get_burger()
                while not(0 < userBurger< 4):
                    self.view.display_invalid_item()
                    userBurger= self.view.get_burger()
                userSide = self.view.get_side()
                while not(10 < userSide < 15):
                    self.view.display_invalid_item()
                    userSide = self.view.get_side()
                userDrink = self.view.get_drink()
                while not (6 < userDrink < 11):
                    self.view.display_invalid_item()
                    userDrink = self.view.get_drink()
                new_item = Create_items(userItem, userBurger, userDrink, userSide)
                item = new_item.createFood()
               
            elif (16 == userItem):
                userNugget = self.view.get_nugget()
                while not (3 < userNugget< 7):
                    self.view.display_invalid_item()
                    userNugget = self.view.get_nugget()
                userSide = self.view.get_side()
                while not (10 < userSide < 15):
                    self.view.display_invalid_item()
                    userSide = self.view.get_side()
                userDrink = self.view.get_drink()
                while not (6 < userDrink < 11):
                    self.view.display_invalid_item()
                    userDrink = self.view.get_drink()
                new_item = Create_items(userItem, userNugget, userDrink, userSide)
                item = new_item.createFood()

            amount = self.view.get_amount()
            while amount< 1:
                self.view.display_invalid_amount()
                amount = self.view.get_amount()

            self.model.add_item(item, amount)

            cont = self.view.get_continue()

            if not cont:
                break

        self.view.cart.display()    