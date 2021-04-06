from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbox



class Window:
    def __init__(self, root):
        self.root = root 

        self.root.wm_title("Filmregister")
        self.root.config(width=750, hight=300)
        self.root.pack_propagate(False)

        self.topFrame = Frame(self.root)
        self.topFrame.pack()    

        self.btnShowM = Button(self.topFrame, text="Visa filmer", width=10, command=self.ShowMovie)
        self.btnShowM.pack(anchor=W, side=LEFT, padx=2, pady=3)

        self.btnAddM = Button(self.topFrame, text="Visa filmer", width=10, command=self.AddMovie)
        self.btnAddM.pack(anchor=W, side=LEFT, padx=2, pady=3)

        self.btnQuit = Button(self.topFrame, text = "Avsluta", width=10, command=self.QuitProgram)
        self.btnQuit.pack(anchor=W, side=LEFT, padx=2, pady=3)

    def ShowMovie(self):
        ""

    def AddMovie(self):
        ""

    def QuitProgram(self):
        msgbox.showinfo("", "Du har valt att avsluta programmet")
        exit()

root = Tk()
Window(root)
root.mainloop()