from cart import Cart
from burger import Burger

class cartView:
    def __init__(self, model: Cart):
        self.model = model

    def display(self):
        print("Item\t\tCost\t\tCal\t\tAmount")
        print(self.model)   
        print()
        print("Final Total: $", end='') 
        finalTotal = round(self.model.calc_total_cost(), 2)
        print(finalTotal)