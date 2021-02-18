from tkinter import *
from tkinter import ttk
import sqlite3

class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        self.UiElements()


    def MakeButton(self):
        menuBtn = Menubutton(self.master, text="Selecione", font=10)
        self.master.config(menu=menuBtn)

        menuBtn.menu = Menu(menuBtn, tearoff=0)
        menuBtn['menu'] = menuBtn.menu
        menuBtn.grid(row=1, column=0)

        menuBtn.menu.add_command(label="Cadastrar", font=7)
        menuBtn.menu.add_command(label="Pesquisar", font=7)


    def Labels(self):
        welcome = Label(self.master, text="Bem vindo ao Meeting Tracker", font=8)
        welcome.grid(row=0, column=0, padx=50, pady=20)


    def UiElements(self):
        self.master.title("Meeting Tracker")
        self.MakeButton()
        self.Labels()


    def main():
        root = Tk()
        root.geometry("350x150")
        app = Window(root)
        root.mainloop()


start = Window.main()

start()

