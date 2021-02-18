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

        subMenu = Menu(menuBtn, tearoff=0)
        searchMenu = Menu(menuBtn, tearoff=0)
        menuBtn.menu.add_cascade(label="Cadastrar", font=7, menu=subMenu)
        menuBtn.menu.add_cascade(label="Pesquisar", font=7, menu=searchMenu)

        subMenu.add_command(label="Alunos")
        subMenu.add_command(label="Salas")
        subMenu.add_command(label="Sala do Café")

        searchMenu.add_command(label="Alunos")
        searchMenu.add_command(label="Salas")
        searchMenu.add_command(label="Sala do Café")
        

    def MakeWindow():
        pass


    def Labels(self):
        welcome = Label(self.master, text="Bem vindo ao Meeting Tracker", font=8)
        welcome.grid(row=0, column=0, padx=65, pady=20)


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

