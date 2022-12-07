from burger import Burger
from burger_combo import Burger_combo
from drink import Drink
from items import Items
from nugget import Nugget
from nugget_combo import Nugget_combo
from side import Side

class Cart:
    """this class stores all of the items that the user orders
    """

    def __init__(self):
        """initializes the Cart
        """
        #dictionary holds the item object as the key and the amount of it as the value
        self.items = {}

    def add_item(self, item, amount):
        """adds an item to the cart

        Args:
            item (item): item the user wants to add to the cart
            amount (int): the amount of the item the user wants to order
        """
        #adds to the list of items a new item and how many are wanted
        self.items[item] = amount

    def calc_total_cost(self):
        """calculates the total cost of everything that was added to the cart

        Returns:
            float: the total value of all the items in the cart
        """
        #initializes the final cost to store the total cost
        finalCost = 0
        for item in self.items:
            #adds the cost of the item times the amount of the item that there is in the cart
            finalCost += item.cost * self.items[item]

        return finalCost

    def __str__(self):
        """returns the name of the items in the cart with the cost, calories, and amount

        Returns:
            string: string that includes all of the items and the details of the order
        """
        #initialize string to store the full string
        string = ''
        for item in self.items:
            amount = self.items[item]
            string += str(item.name) + "\t\t" + str(item.cost) + "\t\t" + str(item.calories) + "\t\t" + str(amount) + "\n"

        return string    
