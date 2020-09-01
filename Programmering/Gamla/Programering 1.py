from tkinter import *
import tkinter.messagebox as msgbox

def go(event) :
    name = entname.get()
    msgbox.showinfo("", "Jävlar va sämst du är på lol " + name + " AHAHA FUCKING NOOB")




root = Tk()

root.config(width=600, height=400, bg="black")
root.wm_title("Da Bruddas Blog")




textrutiboi = Label(root, text="ello bruddas!!!", fg="blue", bg="black")
textrutiboi.pack ()

entname = Entry(root, bg="white")
entname.pack ()

btnpressme = Button(root, bg="white", text="Press me boi", command=go)
btnpressme.pack (pady=20)

root.mainloop()
