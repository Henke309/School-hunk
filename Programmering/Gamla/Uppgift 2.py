from tkinter import *
import tkinter.messagebox as msgbox

def go () :
    info = "Namn: " + entName.get() + "\nAdress: \n" + entAdress.get() + "\nPostnummer, Ort: " + entOrt.get() + "\nTelenr :" + entTele.get()

    msgbox.showinfo("", info)

root = Tk()

lblName = Label(root, text="Namn : ")
lblName.grid(row=0, column=0)

lblAdress = Label(root, text="Adress: ")
lblAdress.grid(row=1, column=0)

lblOrt = Label(root, text="Postnummer &ort: ")
lblOrt.grid(row=2, column=0)

lblTele = Label(root, text="Tele: ")
lblTele.grid(row=3, column=0)

entName = Entry(root)
entName.grid(row=0, column=1)

entAdress = Entry(root)
entAdress.grid(row=1, column=1)

entOrt = Entry(root)
entOrt.grid(row=2, column=1)

entTele = Entry(root)
entTele.grid(row=3, column=1)


btnPopup = Button(root,text="Click here to find out!", command=go)
btnPopup.grid(row=4, column=0, columnspan=2)
root.mainloop()
