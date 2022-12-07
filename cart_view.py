from cart import Cart
from burger import Burger

class Cart_view:
    """Displays the contents of the cart to the screen, the cart contains all of the oprdered items
    """
    def __init__(self, model: Cart):
        """initializes the Cart_view

        Args:
            model (Cart): hold the info on what the user has ordered
        """
        self.model = model

    def display(self):
        """displays the final cart to the screen with the final price
        """
        #header for the cart to show the correct columns
        print("Item\t\tCost\t\tCal\t\tAmount")
        #prints the values in the cart
        print(self.model)   
        print()
        #prints the sum of the costs of all of the items in the cart
        print("Final Total: $", end='') 
        #round the final total to 2 decimal places
        finalTotal = round(self.model.calc_total_cost(), 2)
        print(finalTotal)