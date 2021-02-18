from tkinter import *

class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.UiElements()

    def UiElements(self):
        self.master.title("Meeting Tracker")        


    def main():
        SecondWindow = Tk()
        SecondWindow.geometry("550x350")
        app = Window(SecondWindow)
        SecondWindow.mainloop()


start = Window.main()

start()