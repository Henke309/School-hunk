from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbox


class Main:
    def __init__(self, root):
        self.root = root 

        self.root.wm_title("Telefonbok")
        self.root.config(width=400, height=400)
        self.root.pack_propagate(False)

        self.topFrame = Frame(self.root)
        self.topFrame.pack()

        self.botFrame = Frame(self.root)
        self.botFrame.pack()
        
        # Bygger Top-frame
        self.btnSave = Button(self.topFrame, text="Save", width=10, command=self.saveToFile)
        self.btnSave.pack(anchor=N, side=LEFT, padx=2, pady=3)

        self.btnQuit = Button(self.topFrame, text = "Quit", width=10)
        self.btnQuit.pack(anchor=N, side=LEFT, padx=2, pady=3)

        self.btnInfo = Button(self.topFrame, text="info", width=10)
        self.btnInfo.pack(anchor=N, side=LEFT, padx=2, pady=3)

        # Bygger Bot-Frame
        self.lblName = Label(self.botFrame, text="Namn: ")
        self.lblName.grid(row=0, column=0)

        self.entName = Entry(self.botFrame)
        self.entName.grid(row=0, column=1)

        self.lblTele = Label(self.botFrame, text="Tele: ")
        self.lblTele.grid(row=1, column=0)

        self.entTele = Entry(self.botFrame)
        self.entTele.grid(row=1, column=1)

        self.root.bind("<Return>", lambda x: self.saveToFile())
        self.root.bind("<Enter>", lambda x: self.enterRoot())
        self.root.bind("<Leave>", lambda x: self.leaveRoot())


    def enterRoot(self):
        self.root.config(bg="GREEN")
    
    def leaveRoot(self):
        self.root.config(bg="RED")

    def saveToFile(self):
        file = open("telefonnr.txt", "a")

        file.write(self.entName.get() + "\n" + self.entTele.get() + "\n\n")

        file.close()

        self.entName.delete(0, END)
        self.entTele.delete(0, END)

        msgbox.showinfo("", "Sparad!")
root = Tk()

Main(root)

root.mainloop()
