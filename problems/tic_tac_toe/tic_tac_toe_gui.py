import math
import tkinter.messagebox
from tkinter import *

from algorithms.alpha_beta_pruning import AlphaBetaPruning
from problems.tic_tac_toe.implemented_algorithm import Node, AlgoConfig

tk = Tk()
tk.title("Tic Tac Toe")
tk.resizable(0, 0)

playera = StringVar()
playerb = StringVar()
playera = "You Wins!"
playerb = "You Lose!"

is_started = False
clicked = 0


def switch_button_status(status):
    button1.configure(state=status)
    button2.configure(state=status)
    button3.configure(state=status)
    button4.configure(state=status)
    button5.configure(state=status)
    button6.configure(state=status)
    button7.configure(state=status)
    button8.configure(state=status)
    button9.configure(state=status)


def reset_button_clicked():
    global clicked
    if is_started:
        massage = tkinter.messagebox.askquestion('Reset', 'Are you sure you want to Reset the game?', icon='warning')
        if massage == 'yes':
            reset()
    else:
        tkinter.messagebox.showinfo('warnning', 'the game is not started yet!')
        clicked = 0


def reset():
    global clicked, is_started, initial_node, initial_state

    clicked = 0
    initial_node = Node(initial_state, beta=math.inf, alpha=-math.inf, utility_value=0)
    is_started = False
    button1['text'] = ' '
    button2['text'] = ' '
    button3['text'] = ' '
    button4['text'] = ' '
    button5['text'] = ' '
    button6['text'] = ' '
    button7['text'] = ' '
    button8['text'] = ' '
    button9['text'] = ' '


config = AlgoConfig(max_depth=3)
initial_state = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
initial_node = Node(initial_state, beta=math.inf, alpha=-math.inf, utility_value=0)
alpha_beta_pruning_instance = AlphaBetaPruning(initial_node, config)


def button_clicked(button, row, col):
    global clicked, is_started

    is_started = True
    if button["text"] == " ":
        button["text"] = "X"
        alpha_beta_pruning_instance.initial_node.state[row][col] = 1
        clicked += 1
        check_for_game_status()
        computer_move()

    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


def computer_move():
    global clicked
    try:
        next_node, changed_house = alpha_beta_pruning_instance.minimizer(alpha_beta_pruning_instance.initial_node)
    except Exception:
        pass
    update_game_board(changed_house)
    print(next_node)
    alpha_beta_pruning_instance.initial_node = next_node
    clicked += 1
    check_for_game_status()


def update_game_board(changed_house: list):
    index = changed_house[0] * 3 + changed_house[1]
    buttons[index]["text"] = "O"


def check_for_game_status():
    global clicked
    print(f'clicked: {clicked}')

    print(button3['text'])
    print(button6['text'])
    print(button9['text'])

    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        switch_button_status(status=DISABLED)
        print('GAME FINISHED!')
        msg = tkinter.messagebox.showinfo("Tic-Tac-Toe", playera)
        if msg == 'ok':
            exit()

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        switch_button_status(status=DISABLED)
        print('GAME FINISHED!')
        msg = tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
        if msg == 'ok':
            exit()

    elif clicked == 8:
        msg = tkinter.messagebox.showinfo("Tic-Tac-Toe", "it's a draw!")
        switch_button_status(status=DISABLED)
        if msg == 'ok':
            exit()


button1 = Button(tk, text=" ", font='Times 15 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: button_clicked(button1, 0, 0))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 15 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: button_clicked(button2, 0, 1))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ', font='Times 15 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: button_clicked(button3, 0, 2))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 15 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: button_clicked(button4, 1, 0))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 15 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: button_clicked(button5, 1, 1))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 15 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: button_clicked(button6, 1, 2))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 15 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: button_clicked(button7, 2, 0))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 15 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: button_clicked(button8, 2, 1))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 15 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: button_clicked(button9, 2, 2))
button9.grid(row=5, column=2)

reset_button = Button(tk, text='Rest!', bg='white', fg='black', height=2, width=44,
                      command=lambda: reset_button_clicked())
reset_button.grid(row=6, column=0, columnspan=4)

buttons = [
    button1,
    button2,
    button3,
    button4,
    button5,
    button6,
    button7,
    button8,
    button9,
]

tk.mainloop()
