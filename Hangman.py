from tkinter import *
from tkinter import messagebox
import random

window=Tk()
window.title("Hangman")

uppercaseletter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

categoryList = ['Country', 'Sport', 'Car', 'Place']
wordList = {'Country': ['Iran', 'America', 'England', 'Germany'], 'Sport': ['Football', 'Basketball', 'Swim'], 'Car': [
    'Benz', 'BMW', 'Volkswagen'], 'Place': ['School', 'Home', 'Park']}

photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"), PhotoImage(file="images/hang3.png"),
          PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"), PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"),
          PhotoImage(file="images/hang8.png"), PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]
imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)

def newGame():
    category = random.choice(categoryList)
    word_list = wordList[category]
    the_word = random.choice(word_list).upper()
    messagebox.showinfo("Hangman", "It's a {} Name".format(category))
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))



def guess(letter, counter):
    global numberOfGuesses
    if numberOfGuesses<11:

        txt = list(the_word_withSpaces)
        
        guessed = list(lblWord.get())

        if the_word_withSpaces.count(letter)>0:
            for i in range(len(txt)):
                if txt[i] == letter:
                    guessed[i] = letter
                   
                lblWord.set("".join(guessed))
                if lblWord.get() == the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You Guessed it")
                    newGame()
        else:
                numberOfGuesses+=1
                imgLabel.config(image=photos[numberOfGuesses])
                if numberOfGuesses==11:
                 messagebox.showwarning("Hangman", "Game Over")
    


buttons = [0 for _ in range(len(uppercaseletter))]
counter = 0
n=0
for letter in uppercaseletter:
    buttons[counter] = Button(window, text=letter, command=lambda letter=letter: guess(letter, counter), font=("Helvetica 18"), width=4)
    buttons[counter].grid(row=1+n//9, column=n%9)
    n += 1
    counter += 1

Button(window, text="new\nGame", command=lambda:newGame(),font=("Helvetica 10 bold")).grid(row=3, column=8, sticky="NSWE")

newGame()    
window.mainloop()