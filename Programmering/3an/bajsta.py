from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbox
from inl2class_HenrikNguyen import *
import pickle

class Window:
    def __init__(self, root):
        self.root = root 
        self.Movielist = pickle.load(open("Movies.p", "rb"))

        self.root.wm_title("(Skicka Mail) Klient")
        self.root.config(width=400, height=400)
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
        self.btnSave = Button(self.topFrame, text="Logga in", width=10, command=self.SaveToFile)
        self.btnSave.pack(anchor=N, side=LEFT, padx=2, pady=3)

        self.btnQuit = Button(self.topFrame, text = "Avsluta", width=10, command=self.QuitProgram)
        self.btnQuit.pack(anchor=N, side=LEFT, padx=2, pady=3)

        self.btnInfo = Button(self.topFrame, text="Info", width=10, command=self.Infobox)
        self.btnInfo.pack(anchor=N, side=LEFT, padx=2, pady=3)

        self.btnShowMovies = Button(self.topFrame, text="Visa filmlistan", command=self.ShowMovielistBox)
        self.btnShowMovies.pack(anchor=N, side=LEFT,padx=2, pady=3 )

        # Bygger Bot-Frame
        self.lblReg = Label(self.botFrame, text="Lägg till en film")
        self.lblReg.grid(row=1, columnspan= 2, pady=3)

        self.lblTitle = Label(self.botFrame, text="Title: ")
        self.lblTitle.grid(row=2, column=0, pady=1)

        self.entTitle = Entry(self.botFrame)
        self.entTitle.grid(row=2, column=1, pady=1)

        self.lblRelease = Label(self.botFrame, text="År: ")
        self.lblRelease.grid(row=3, column=0, pady=1)

        self.entRelease = Entry(self.botFrame)
        self.entRelease.grid(row=3, column=1, pady=1)

        self.lblGenre = Label(self.botFrame, text="Genre: ")
        self.lblGenre.grid(row=4, column=0, pady=1)

        self.entGenre = Entry(self.botFrame)
        self.entGenre.grid(row=4, column=1, pady=1)

        self.lblReg = Label(self.botFrame, text="-----")
        self.lblReg.grid(row=5, columnspan= 2, pady=5)

        self.root.bind("<Return>", lambda x: self.SaveToFile())
        self.root.bind("<Return>", lambda x: self.Infobox())
        self.root.bind("<Return>", lambda x: self.QuitProgram())

        #Bygger Top2-Frame
        self.btnRemove = Button(self.top2Frame, text="Ta bort", width=10, command=self.Remove)
        self.btnRemove.pack(anchor = N, side=LEFT , pady=3)

        #Bygger Bot2-Frame

        self.lblReg = Label(self.bot2Frame, text="Ta bort en film")
        self.lblReg.grid(row=0, columnspan= 2, pady=3)

        self.lblRemove = Label(self.bot2Frame, text="Filmens Nr: ")
        self.lblRemove.grid(row=1, column=0, pady=1)

        self.entRemove = Entry(self.bot2Frame)
        self.entRemove.grid(row=1, column=1, pady=1)

        self.lblReg = Label(self.bot2Frame, text="-----")
        self.lblReg.grid(row=2, columnspan= 2, pady=5)

        #Bygger Top3-Frame
        self.btnMark = Button(self.top3Frame, text="Markera sedd", width=20, command=self.mark)
        self.btnMark.pack(anchor = N, side=LEFT , pady=3)

        #Bygger Bot3-Frame
        self.lblMark = Label(self.bot3Frame, text="Filmens Nr: ")
        self.lblMark.grid(row=1, column=0, pady=1)

        self.entMark = Entry(self.bot3Frame)
        self.entMark.grid(row=1, column=1, pady=1)


    def mark(self):
        try:
            self.Movielist[int(self.entMark.get()) - 1].seen = True
            pickle.dump(Movielist, open("Movies.p", "wb"))
        
        except ValueError:
            msgbox.showinfo("Felmeddelande", "Endast Siffor \nInga bokstäver eller någon tom ruta")             

    def SaveToFile(self):
        self.Movielist.append(Movie(self.entTitle.get(), self.entRelease.get(), self.entGenre.get() ))
        self.entTitle.delete(0, END)
        self.entRelease.delete(0, END)
        self.entGenre.delete(0, END)
        pickle.dump(Movielist, open("Movies.p", "wb"))

        msgbox.showinfo("", "Sparad!")
    
    def Infobox(self):
        
        info = Tk()
        info.config(width=200, height=200)
        info.pack_propagate(False)

        removeinfotxt = "Filmens Nr:              \nOvan ser du 'filmens nr' samt dess textruta.\nI textrutan ska du skriva in filmens nummer,\n vilket du kan hitta om du trycker på knappen 'Visa Filmlistan'.\nNär knappen är tryckt kommer en ny ruta upp med alla filmer samt dess egenskaper.\nUnder Nr hittar du filmens nummer, skriv nummret som står brevid filmen du vill ha boort i textrutan. Sedan klicka på knappen 'Ta bort'"
        self.btnRemoveInfo = Button(info, text="Info: Ta bort", width=10, command=lambda:msgbox.showinfo("Hur man tar bort en film", removeinfotxt))
        self.btnRemoveInfo.pack(anchor=N, side=LEFT, padx=2, pady=3)
        seeninfotxt = "Filmens Nr:              \nOvan ser du 'filmens nr' samt dess textruta.\nI textrutan ska du skriva in filmens nummer,\n vilket du kan hitta om du trycker på knappen 'Visa Filmlistan'.\nNär knappen är tryckt kommer en ny ruta upp med alla filmer samt dess egenskaper.\nUnder Nr hittar du filmens nummer, skriv nummret som står brevid filmen som du vill markera i textrutan. Sedan klicka på knappen 'Markera Sedd'"
        self.btnSeenInfo = Button(info, text="Info: Markera sedd", width=10, command=lambda:msgbox.showinfo("Hur man markerar en sedd film", seeninfotxt))
        self.btnSeenInfo.pack(anchor=N, side=LEFT, padx=2, pady=3)
        
        info.mainloop()
        
    def Remove(self):
        try:
            del self.Movielist[int(self.entRemove.get()) - 1]
            pickle.dump(Movielist, open("Movies.p", "wb"))        
        except ValueError:
            msgbox.showinfo("Felmeddelande", "Endast Siffor \nInga bokstäver eller någon tom ruta")

    def InfoRemove(self):
        msgbox.showinfo("", "No") 

    def InfoSeen(self):
        msgbox.showinfo("", "No")        

    def QuitProgram(self):
        msgbox.showinfo("", "Du har valt att avsluta programmet")
        exit()
            


        show.mainloop()

        #print(len(self.Movielist)) #checkar ifall det funkar :D


root = Tk()

Window(root)

root.mainloop()
