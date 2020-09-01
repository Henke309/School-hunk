from tkinter import *
import tkinter.messagebox as msgbox

def go():

    if not entAge.get().isnumeric():
        msgbox.showerror("", "Skriv in ett tal! Jävla noob...")
    else:
        age = int(entAge.get())

        if age < 6:
            msgbox.showinfo("Lol boi", "Du var inte så gammal kiddo!")
        elif 6 <= age < 15:
            msgbox.showinfo("", "Cykla jävla kiddo!")
        elif 15<= age < 18:
            msgbox.showinfo("", "Ey tja jävla moppebög! xD")
        else:
            msgbox.showinfo("", "Time to drive a MOTHERF***ing CAR BROTHER")
        
root= Tk()

lblAge= Label(root, text="Ålder:")
lblAge.pack()

entAge = Entry(root)
entAge.pack()

btnPress = Button(root, text ="lol?", command=go)
btnPress.pack()

root.mainloop()
