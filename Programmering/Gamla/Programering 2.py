from tkinter import *
import tkinter.messagebox as msgbox

def savetofile():
    f = open("telefonnummer.txt", "a")
    f.write(entName.get() + " " + entTele.get() + "\n")
    f.close()

root = Tk()

lblName = Label(root, text="Namn : ")
lblName.grid(row=0, column=0)

lblTele = Label(root, text="Tele: ")
lblTele.grid(row=1,column=0)

entName = Entry(root)
entName.grid(row=0, column=1)

entTele = Entry(root)
entTele.grid(row=1, column=1)

btnSave = Button(root, text="Spara till fil!", command=savetofile)
btnSave.grid(row=2, column=0, columnspan=2)


root.mainloop()
