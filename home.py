import PySimpleGUI as sg #allows for use of GUI

#layout for the homescreen
layout = [

    [sg.Button("Burgers"), sg.Button("Cart")],
    [sg.Button("Nuggets")],
    [sg.Button("Drinks")],
    [sg.Button("Sides")],
    [sg.Button("Combo")],
    [sg.Exit()],
]

#creates the window for the user to see
window = sg.Window("McDonald's Ordering", layout)

#this runs continuously until the user clicks exit or the x button
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Burgers":
        sg.popup_error("Burgers Not yet implemented")
    if event == "Nuggets":
        sg.popup_error("Nuggets Not yet implemented")
    if event == "Drinks":
        sg.popup_error("Drinks Not yet implemented")
    if event == "Sides":
        sg.popup_error("Sides Not yet implemented")   
    if event == "Combo":
        sg.popup_error("Combo Not yet implemented")
    if event == "Cart":
        sg.popup_error("Cart Not yet implemented")       
#closes window           
window.close()       

