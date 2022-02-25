import tkinter as tk
from tkinter import ttk
from random import randint

root=tk.Tk()
root.title('Игровой автомат')
root.resizable(False, False)

hello_lable = ttk.Label(root, text='Добро пожаловать в казино')
hello_lable.grid(row=0, column=0, columnspan=2)

main_frame = ttk.Frame(root, width=200, height=100)
main_frame.grid()

def draw_board():
    input(termcolor.colored('Дерните за рычаг нажав Enter: ','yellow'))
    board = list(range(1, 5))
    board[0] = randint(1,5)
    board[1] = randint(1,5)
    board[2] = randint(1,5)
    board[3] = randint(1,5)

    # time.sleep(2)
    # print(termcolor.colored('-' * 17, 'blue'))
    # print('|', board[0], '|', board[1],'|', board[2], '|', board[3], '|')
    # print(termcolor.colored('-' * 17, 'magenta'))
    return board

board_frame_1 = ttk.Frame(main_frame, borderwidth=15, relief="ridge", padding=(20,10,10,15))
board_frame_1.grid(row=1, column=1)

board_frame_2 = ttk.Frame(main_frame, borderwidth=15, relief="ridge", padding=(20,10,10,15))
board_frame_2.grid(row=1, column=2)

board_frame_3 = ttk.Frame(main_frame, borderwidth=15, relief="ridge", padding=(20,10,10,15))
board_frame_3.grid(row=1, column=3)

board_frame_4 = ttk.Frame(main_frame, borderwidth=15, relief="ridge", padding=(20,10,10,15))
board_frame_4.grid(row=1, column=4)

label_board_1 = ttk.Label(board_frame_1)
label_board_1.grid(row=1, column=1)

label_board_2 = ttk.Label(board_frame_2)
label_board_2.grid(row=1, column=2)

label_board_3 = ttk.Label(board_frame_3)
label_board_3.grid(row=1, column=3)

label_board_4 = ttk.Label(board_frame_4)
label_board_4.grid(row=1, column=4)

button_board = ttk.Button(main_frame, text='Enter', command=draw_board)
button_board.grid(row=2, column=2, columnspan=2)


input_frame = ttk.Frame(root, width=200, height=100)
input_frame.grid()

username_label = ttk.Label(input_frame, text='Ставка: ')
username_label.grid(row=3, column=0, padx=(5, 10))

entry_credit = ttk.Entry(input_frame)
entry_credit.grid(row=3,column=2, sticky='W')

button_credit = ttk.Button(input_frame, text='Enter')
button_credit.grid(row=4, column=2, columnspan=2)



frame_money = ttk.Frame(root, width=200, height=100)
frame_money.grid()

label_money = ttk.Label(frame_money, text='Кошелек: ')
label_money.grid(row=5, column=0)

label_bank = ttk.Label(frame_money, text='Банк: ')
label_bank.grid(row=6, column=0)

label_bank_casino = ttk.Label(frame_money, text='Банк казино: ')
label_bank_casino.grid(row=7, column=0)


frame_continue = ttk.Frame(root, width=200, height=100)
frame_continue.grid()

label_continue = ttk.Label(frame_continue, text='Продолжить игру?')
label_continue.grid(row=8, column=0)

button_yes = ttk.Button(frame_continue, text='Да')
button_yes.grid(row=8, column=1, columnspan=2)

button_no = ttk.Button(frame_continue, text='Нет')
button_no.grid(row=8, column=3, columnspan=2)


root.mainloop()