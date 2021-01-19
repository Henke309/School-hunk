from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbox
from tkinter import scrolledtext

class Window:
    def __init__(self, root):
        self.root = root 

        self.root.wm_title("(Skicka Mail) Klient")
        self.root.config(width=1000, height=500)
        self.root.pack_propagate(False)

        self.topFrame = Frame(self.root)
        self.topFrame.pack()

        self.botFrame = Frame(self.root)
        self.botFrame.pack()

        self.top2Frame = Frame(self.root)
        self.top2Frame.pack()

        self.bot2Frame = Frame(self.root)
        self.bot2Frame.pack()

        self.top3Frame = Frame(self.root)
        self.top3Frame.pack()     

        self.bot3Frame = Frame(self.root)
        self.bot3Frame.pack()        

        # Bygger Top-frame
        self.btnLogin = Button(self.topFrame, text="Logga in", width=10, command=self.Login)
        self.btnLogin.pack(anchor=N, side=LEFT, padx=2, pady=3)

        self.btnQuit = Button(self.topFrame, text = "Avsluta", width=10, command=self.QuitProgram)
        self.btnQuit.pack(anchor=N, side=LEFT, padx=2, pady=3)

        # Bygger Bot-Frame
        self.lblReg = Label(self.botFrame, text="Inlogg...")
        self.lblReg.grid(row=1, columnspan= 2, pady=3)

        self.lblTitle = Label(self.botFrame, text="E-Mail: ")
        self.lblTitle.grid(row=2, column=0, pady=1)

        self.entTitle = Entry(self.botFrame)
        self.entTitle.grid(row=2, column=1, pady=1)

        self.lblRelease = Label(self.botFrame, text="Lösenord: ")
        self.lblRelease.grid(row=3, column=0, pady=1)

        self.entRelease = Entry(self.botFrame)
        self.entRelease.grid(row=3, column=1, pady=1)

        self.lblReg = Label(self.botFrame, text="-----")
        self.lblReg.grid(row=5, columnspan= 2, pady=5)

        self.lblReg = Label(self.botFrame, text="Efter att du har loggat in så kan du fortsätta här nere för att skicka ett mail.")
        self.lblReg.grid(row=6, columnspan= 2, pady=5)

        self.root.bind("<Return>", lambda x: self.Login())
        self.root.bind("<Return>", lambda x: self.QuitProgram())


        #Bygger Top2-Frame
        self.lblReg = Label(self.top2Frame, text="Skriv ditt mail nedan")
        self.lblReg.grid(row=1, columnspan= 2, pady=3)

        #Bygger Bot2-Frame

        self.lblReg = Label(self.bot2Frame, text="Till: ")
        self.lblReg.grid(row=0, column=0, pady=1)

        self.enttill = Entry(self.bot2Frame)
        self.enttill.grid(row=0, column=1, pady=1)

        self.lblSubject = Label(self.bot2Frame, text="Ämne: ")
        self.lblSubject.grid(row=1, column=0, pady=1)

        self.entSubject = Entry(self.bot2Frame)
        self.entSubject.grid(row=1, column=1, pady=1)

        self.lblText = Label(self.bot2Frame, text="Text: ")
        self.lblText.grid(row=2, column=0, pady=1)

        self.WrittenText = scrolledtext.ScrolledText(root, wrap = WORD, width = 25, height = 10, font = ("Times New Roman", 9))
        self.WrittenText.grid(row=2, column=10, pady=250, padx=850)
        self.WrittenText.focus()

        self.lblReg = Label(self.bot2Frame, text="-----")
        self.lblReg.grid(row=3, columnspan= 2, pady=5)

    def Login(self):
        pass

    def QuitProgram(self):
        msgbox.showinfo("", "Du har valt att avsluta programmet")
        exit()

root = Tk()
Window(root)

root.mainloop()
