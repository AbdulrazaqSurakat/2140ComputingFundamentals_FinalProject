from burger import Burger
from burger_combo import Burger_combo
from drink import Drink
from items import Items
from nugget import Nugget
from nugget_combo import Nugget_combo
from side import Side

class Cart:

    def __init__(self):
        self.items = {}

    def add_item(self, item, amount):
        #adds to the list of items a new item and how many are wanted
        self.items[item] = amount

    def calc_total_cost(self):
        finalCost = 0
        for item in self.items:
            #adds the cost of the item times the amount of the item that there is in the cart
            finalCost += item.cost * self.items[item]

        return finalCost

    def __str__(self):
        string = ''
        for item in self.items:
            amount = self.items[item]
            string += str(item.name) + "\t\t" + str(item.cost) + "\t\t" + str(item.calories) + "\t\t" + str(amount) + "\n"

        return string    
