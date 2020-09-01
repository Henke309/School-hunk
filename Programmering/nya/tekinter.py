from tkinter import *
import tkinter.messagebox as msgbox
def hello():
    msgbox.showinfo("Rubriken", "hej och välkommen {}".format(entName.get())) 



root = Tk()

root.wm_title("ett exempel")
root.config(width=400, height=400)
root.pack_propagate(FALSE)

lblTest = Label (root, text="Namn:") 
lblTest.pack()

entName = Entry(root)
entName.pack()

btnHello = Button(root, text="hejsan!", command=hello)
btnHello.pack()

root.mainloop()

