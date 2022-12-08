from menu_view import Menu_view
from cart import Cart
from controller import Controller

#creates the cart that will store all of the ordered items
theCart = Cart()

#creats the menu view so the program can get its first input
view = Menu_view(theCart)

#create the controller that interacts with the view and the cart
theController = Controller(theCart, view)

#controller runs the program until user wants to end ordering
theController.run_menu()