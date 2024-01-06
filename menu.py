import tkinter as tk
from tkinter import messagebox
from tkinter import font
import os
from theme import theme


def run_ttt():
    os.system('py ttt.py')

def run_hm():
    os.system('py Hangman.py')

def run_sp():
    os.system('py space.py')

def run_2048():
    os.system('py 2048.py')

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self._frame = None
        self.switch_frame(MainMenu)

    def switch_frame(self, frame_class):     
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()           
        self._frame = new_frame
        self._frame.pack()

    def show_info(static):
        messagebox.showinfo("Info", "Author:Amir.H")
                                
    def quit(self):
        self.destroy()


class MainMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="Game Center",font=('Times New Roman',38)).pack(side="top", fill="x", pady=55, padx=75)

        tk.Button(self, text="Space Invaders",font=theme.fontMenuButton,command=run_sp,
            borderwidth=theme.borderwidth, foreground=theme.foreground, background=theme.backgroud).pack(pady=5)
        
        tk.Button(self, text='Tic Tac Toe',font=theme.fontMenuButton,command=run_ttt,
            borderwidth=theme.borderwidth, foreground=theme.foreground, background=theme.backgroud).pack(pady=5)
        
        tk.Button(self, text="HangMan",font=theme.fontMenuButton,command=run_hm,
            borderwidth=theme.borderwidth, foreground=theme.foreground, background=theme.backgroud).pack(pady=5)
        
        tk.Button(self, text='2048',font=theme.fontMenuButton,command=run_2048,
            borderwidth=theme.borderwidth, foreground=theme.foreground, background=theme.backgroud).pack(pady=5)
        
        tk.Button(self, text="QUIT", font=('Arial',12), borderwidth=theme.borderwidth, foreground='#66FCF1', background='#1F2833',
                  command=lambda: master.quit()).pack(pady=35)
        
        tk.Button(self, text="ABOUT",borderwidth=theme.borderwidth, foreground='#66FCF1', background='#1F2833',
                  command=lambda: master.show_info()).pack(pady=15)


if __name__ == "__main__":
    app = SampleApp()
    app.resvar = '800x600'
    app.configure(bg='#101820')
    app.geometry(app.resvar)
    app.resizable(0, 0)
    app.mainloop()