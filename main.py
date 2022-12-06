from menu_view import Menu_view
from cart import Cart
from controller import Controller

theCart = Cart()
view = Menu_view(theCart)
theController = Controller(theCart, view)

theController.run_menu()