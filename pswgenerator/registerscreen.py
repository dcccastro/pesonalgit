from tkinter import *

class WindowTwo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.UiElements()

    def UiElements(self):
        self.master.title("Meeting Tracker") 
        self.ShowButtons()
        self.ShowLabels()
        self.ShowEntries()

    def ShowButtons(self):
        backBtn = Button(self.master, text="Back")
        backBtn.grid(row=0, column=0, padx=10, pady=5)

    def ShowLabels(self):
        pass

    def ShowEntries(self):
        pass

    def main():
        SecondWindow = Tk()
        SecondWindow.geometry("550x350")
        app = WindowTwo(SecondWindow)
        SecondWindow.mainloop()


WindowTwo.main()