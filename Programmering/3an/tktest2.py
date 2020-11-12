from tkinter import *
import tkinter.messagebox as msgbox

class Main():
    def __init__(self, root):
        self.root = root
        self.root.wm_title("Telefonboken v0.9")


        #Skapar frames    
        self.topFrame = Frame(self.root)
        self.topFrame.pack()

        self.bottomFrame = Frame(self.root)
        self.bottomFrame.pack(side=BOTTOM)

        #TopFrame
        self.buttonSave = Button(self.topFrame, text="Spara", width=10, command=self.saveToFile)
        self.buttonSave.pack(anchor=N, side=LEFT , padx=2, pady=2)

        self.buttonQuit = Button(self.topFrame, text="Avsluta", width=10, command=self.root.destroy)
        self.buttonQuit.pack(anchor=N, side=LEFT , padx=2, pady=2)

        self.buttonInfo = Button(self.topFrame, text="Information", width=10, command=self.showinfo)
        self.buttonInfo.pack(anchor=N, side=LEFT , padx=2, pady=2)

        #BottomFrame
        self.nameLabel= Label(self.bottomFrame, text="Namn")
        self.nameLabel.grid(row=0, column=0, sticky=E)

        self.phoneNoLabel = Label(self.bottomFrame, text="Telefonnummer")
        self.phoneNoLabel.grid(row=1, column=0)

        self.nameEntry = Entry(self.bottomFrame)
        self.nameEntry.grid(row=0, column=1)

        self.phoneNoEntry = Entry(self.bottomFrame)
        self.phoneNoEntry.grid(row=1, column=1)

    def saveToFile(self):
        toFile = open("Phonebook.txt", "a")
        toFile.write(self.nameEntry.get() + " " + self.phoneNoEntry.get() + "\n")
        toFile.close()

        msgbox.showinfo("Sparat", "Telefonnumret är spart!")

        self.nameEntry.delete(0, END)
        self.phoneNoEntry.delete(0, END)

    def showInfo(self):
        pass


if __name__ == "__main__":
    root = Tk()
    Main(root)
    root.mainloop()