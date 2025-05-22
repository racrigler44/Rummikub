from tkinter import *
from validation_input_hand import validate_colornumber_input
from validation_input_board import validate_colornumber_input_board


def show_result_screen():
    # Hide input screen
    input_frame.pack_forget()
    
    # Clear the result screen in case it's already created
    for widget in result_frame.winfo_children():
        widget.destroy()

    Label(result_frame, text="Inputs Confirmed", font=("Arial", 16)).pack(pady=10)
    Label(result_frame, text=f"Hand: {hand_input}").pack()
    Label(result_frame, text=f"Board: {board_input}").pack()

    # 👉 Run the algorithm
    Label(result_frame, text="Updated Board:").pack(pady=5)
    Label(result_frame, text=new_board).pack()

    Button(result_frame, text="Back", command=show_input_screen).pack(pady=10)
    result_frame.pack()


def show_input_screen():
    result_frame.pack_forget()
    input_frame.pack()


def submit_all():
    global hand_input, board_input
    hand_input = e1.get()
    board_input = e2.get()

    valid_hand, msg_hand = validate_colornumber_input(hand_input)
    valid_board, msg_board = validate_colornumber_input_board(board_input)

    if valid_hand and valid_board:
        show_result_screen()
    else:
        error_msg = ""
        if not valid_hand:
            error_msg += f"Hand Error: {msg_hand}\n"
        if not valid_board:
            error_msg += f"Board Error: {msg_board}"
        error_label.config(text=error_msg)


# Main window
master = Tk()
master.title("Tiles Input")

hand_input = ""
board_input = ""

# Input Frame
input_frame = Frame(master)
Label(input_frame, text="Enter your hand:").grid(row=0, column=0)
Label(input_frame, text="Enter the board:").grid(row=1, column=0)

e1 = Entry(input_frame, width=50)
e2 = Entry(input_frame, width=50)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

submit_btn = Button(input_frame, text="Submit All", command=submit_all)
submit_btn.grid(row=2, column=1, pady=10)

error_label = Label(input_frame, text="", fg="red")
error_label.grid(row=3, columnspan=3)

input_frame.pack(padx=20, pady=20)

# Result Frame (initially hidden)
result_frame = Frame(master)

master.mainloop()
