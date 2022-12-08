from cart import Cart
from menu_view import Menu_view
from create_items import Create_items

class Controller:
    """this controls what is run in the program, calls for the separate functions to run
    """

    def __init__(self, model: Cart, view: Menu_view):
        """initializes the object

        Args:
            model (Cart): holds the information about the ordered items
            view (Menu_view): allows for the program to display the menu and the cart
        """
        self.model = model
        self.view = view

    def run_menu(self):
        """runs the ordering process for the 
        """
        #this while loop makes the menu display for the user and then also gets values form the user
        while True:

            #displays the menu to the user
            self.view.displayMenu()
            #gets the item that the user wants to order
            userItem = self.view.get_item()

            #if the entered value for the item was not in the correct range then display error then get new value
            while (not (0 < userItem < 17)):
                self.view.display_invalid_item()
                userItem = self.view.get_item()

            #runs only if the user chose a non-combo item
            if (0 < userItem < 15):
                #creates the create_item which then creates the food object
                new_item = Create_items(userItem)
                item = new_item.createFood()

            #runs only if the user wants to order the burger combo    
            elif (15 == userItem):

                #get what burger the user wants
                userBurger = self.view.get_burger()
                #display if input error
                while not(0 < userBurger< 4):
                    self.view.display_invalid_item()
                    userBurger= self.view.get_burger()
                
                #gets the wanted side from the user
                userSide = self.view.get_side()
                #display if input error
                while not(10 < userSide < 15):
                    self.view.display_invalid_item()
                    userSide = self.view.get_side()

                #gets drink from the user    
                userDrink = self.view.get_drink()
                #display if input error
                while not (6 < userDrink < 11):
                    self.view.display_invalid_item()
                    userDrink = self.view.get_drink()

                #the object create_item is made with all selected sub-items where the food object for the combo is created    
                new_item = Create_items(userItem, userBurger, userDrink, userSide)
                item = new_item.createFood()

            #runs if the user wanted a nugget combo   
            elif (16 == userItem):
                #gets what nugget the user wants
                userNugget = self.view.get_nugget()
                #display if input error
                while not (3 < userNugget< 7):
                    self.view.display_invalid_item()
                    userNugget = self.view.get_nugget()

                #gets what side the user wants    
                userSide = self.view.get_side()
                #display if input error
                while not (10 < userSide < 15):
                    self.view.display_invalid_item()
                    userSide = self.view.get_side()

                #gets drink from the user    
                userDrink = self.view.get_drink()
                #display if input error
                while not (6 < userDrink < 11):
                    self.view.display_invalid_item()
                    userDrink = self.view.get_drink()

                #the object create_item is made with all selected sub-items where the food object for the combo is created     
                new_item = Create_items(userItem, userNugget, userDrink, userSide)
                item = new_item.createFood()

            #gets the amount of the item the user wants to order
            amount = self.view.get_amount()

            #makes sure the inputted amount is positive, displays error message then asks for a new valid value
            while amount< 1:
                self.view.display_invalid_amount()
                amount = self.view.get_amount()

            #adds the item the user created to the cart
            self.model.add_item(item, amount)

            #asks the user if they want to continue ordering
            cont = self.view.get_continue()

            #if the user is done ordering this runs to end the while loop this is in
            if not cont:
                break

        #displays the cart with all of the ordered items
        self.view.cart.display()    