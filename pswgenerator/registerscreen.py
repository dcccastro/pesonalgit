from tkinter import *

class WindowTwo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.UiElements()


    def UiElements(self):
        self.master.title("Meeting Tracker") 
        self.ShowButtons()
        self.ShowLabels("Nome: ", 0)
        self.ShowEntries(1)


    def ShowButtons(self):
        backBtn = Button(self.master, text="Back")
        backBtn.grid(row=0, column=0, padx=10, pady=5)

        submitBtn = Button(self.master, text="Cadastrar")
        submitBtn.grid(row=1, column=5, padx=10, pady=5)

        submitRoomBtn = Button(self.master, text="Cadastrar Sala")
        submitRoomBtn.grid(row=2, column=5, padx=10, pady=5)

        submitCafeBtn = Button(self.master, text="Cadastrar Sala do Café")
        submitCafeBtn.grid(row=3, column=5, padx=10, pady=5)


    def ShowLabels(self, textname, columnNum):
        labels = []
        for n in range(1, 4):
            newLabel = Label(self.master, text=textname).grid(row=n, column=columnNum, padx=10)
            labels.append(newLabel)

        secondNameLabel = Label(self.master, text="Sobrenome: ")
        secondNameLabel.grid(row=1, column=3, padx= 10)

        eventLabel = Label(self.master, text="Lotação: ")
        eventLabel.grid(row=2, column=3, padx= 10)


    def ShowEntries(self, number):
        entries = []
        for n in range(1, 4):
            newEntry = Entry(self.master).grid(row=n, column=number, padx=10, pady=10)
            entries.append(newEntry)  
        
        LastName = Entry(self.master).grid(row=2, column=4, padx=10, pady=10)
        roomCapacity = Entry(self.master).grid(row=1, column=4, padx=10, pady=10)


    def main():
        SecondWindow = Tk()
        SecondWindow.geometry("600x200")
        app = WindowTwo(SecondWindow)
        SecondWindow.mainloop()


WindowTwo.main()