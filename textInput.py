from tkinter import *
from validation_input_hand import validate_colornumber_input  # Import from separate file
from validation_input_board import validate_colornumber_input_board  # Import from separate file
master = Tk()
master.title("Tiles Input")

Label(master, text="Enter your hand:").grid(row=0)
Label(master, text="Enter the board:").grid(row=1)

e1 = Entry(master, width=50)
e2 = Entry(master, width=50)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def button_click():
    hand = e1.get()
    valid, message = validate_colornumber_input(hand)
    if valid:
        print("Hand is valid:", hand)
    else:
        print("Invalid hand input:", message)
button = Button(master, text="Click me!", command=button_click)
button.grid(row=0, column=2)

def button_click():
    hand = e2.get()
    valid, message = validate_colornumber_input_board(hand)
    if valid:
        print("Hand is valid:", hand)
    else:
        print("Invalid hand input:", message)
button = Button(master, text="Click me!", command=button_click)
button.grid(row=1, column=2)
mainloop()