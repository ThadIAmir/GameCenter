from tkinter import *
import random
from theme import theme

# next turn for each player
def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == '' and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + ' turn'))

            elif check_winner() is True:
                label.config(text=(players[0] + ' wins'))

            elif check_winner() == 'Toe!':
                for row in range(3):
                    for column in range(3):
                        buttons[row][column].config(bg='blue')
                label.config(text='Toe!')

        else:
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + ' turn'))

            elif check_winner() is True:
                label.config(text=(players[1] + ' wins'))

            elif check_winner() == 'Toe!':
                for row in range(3):
                    for column in range(3):
                        buttons[row][column].config(bg='blue')
                label.config(text='Toe!')

# check winner in rows and columns or toe!
def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            buttons[row][0].config(bg='green')
            buttons[row][1].config(bg='green')
            buttons[row][2].config(bg='green')
            return True
    
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            buttons[0][column].config(bg='green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg='green')
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True
    
    elif empty_spaces() is False:
        for row in range(3):
                    for column in range(3):
                        buttons[row][column].config(bg='blue')
        return 'Toe!'

    else:
        return False

# check if we have empty space or not
def empty_spaces():
    space = 9 
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                space -= 1
    if space == 0:
        return False
    else:
        return True

# start again a new game
def new_game():
    
    global player
    
    player = random.choice(players)
    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = '', bg = 'white')

# config the screen
playGroud = Tk()
playGroud.title("Tic Tac Toe")
playGroud.config(bg='white')


#players
players = ["x", "o"]
player = random.choice(players)

# config label and button
label = Label(text=player + " turn", font=("consolas", 40), borderwidth=theme.borderwidth, foreground=theme.foreground, background=theme.backgroud)
label.pack(side="top")
reset_button = Button(text='restart game', font=(
    "consolas", 20), command=new_game,borderwidth=theme.borderwidth, foreground=theme.foreground, background=theme.backgroud)
reset_button.pack(side='top', pady=5)



# button lists
buttons = [[0 for _ in range(3)] for _ in range(3)]

frame = Frame(playGroud)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text='', font=(
            "consolas", 40), width=5, height=2, command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].config(bg='white')
        buttons[row][column].grid(row=row, column=column)

playGroud.mainloop()