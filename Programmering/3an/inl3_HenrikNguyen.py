from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.messagebox as msgbox



class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.persons = []
        self.wm_title("Filmregister")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Start, Add, Show):
            frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Start)

    def show_frame(self, cont):
        frame = self.frames[cont]

        if cont == Show:
            self.frames[cont].update(self.container, self)

        frame.tkraise()

    def QuitProgram(self):
        msgbox.showinfo("", "Du har valt att avsluta programmet")
        exit()

class Start(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Hunkebois filmregister")
        label.pack(pady=10, padx=10)

        buttonAdd = tk.Button(self, text="Lägg till en film", command=lambda: controller.show_frame(Add))
        buttonAdd.pack()

        buttonShow = tk.Button(self, text="visa alla filmer", command=lambda: controller.show_frame(Show))
        buttonShow.pack()

        buttonQuit = tk.Button(self, text="Avsluta", command=lambda: controller.quit())
        buttonQuit.pack()

class Add(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        titleLabel = tk.Label(self, text="Title: ")
        titleLabel.grid(row=0, column=0)

        releaseLabel = tk.Label(self,text="Release: ")
        releaseLabel.grid(row=1, column=0)

        self.titleEntry = tk.Entry(self)
        self.titleEntry.grid(row=0, column=1)
        
        self.releaseEntry = tk.Entry(self)
        self.releaseEntry.grid(row=1, column=1)

        buttonSave = tk.Button(self, text="Spara", command=self.save)
        buttonSave.grid(row=2, column=0, columnspan=2)

        buttonBack = tk.Button(self, text="Tillbaka", command=lambda: self.controller.show_frame(Start))
        buttonBack.grid(row=3, column=0, columnspan=2)

    def save(self):
        ""

class Show(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.build(parent, controller)
        
        buttonBack = tk.Button(self, text="Tillbaka", command=lambda: controller.show_frame(Start))
        buttonBack.pack()
