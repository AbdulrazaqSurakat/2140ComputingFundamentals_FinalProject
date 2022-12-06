import unittest
from burger import Burger
from burger_combo import Burger_combo
from nugget import Nugget
from nugget_combo import Nugget_combo 
from drink import Drink
from side import Side
from cart import Cart
from cart_view import Cart_view
from create_items import Create_items

userBurger = Burger("CheeseBurger", 8.99, 890)
userNugget = Nugget("Nuggets",2.99, 200)
userDrink = Drink("Sprite",3.99, 100)
userSide = Side(f"Onion Rings", 4.99, 60)

class Test(unittest.TestCase):

    def test_burger(self):
        self.assertIsInstance(userBurger, Burger)

    def test_drink(self):
        self.assertIsInstance(userDrink, Drink)

    def test_nugget(self):
        self.assertIsInstance(userNugget, Nugget)

    def test_side(self):
        self.assertIsInstance(userSide, Side)

if __name__=="__main__":
    unittest.main()