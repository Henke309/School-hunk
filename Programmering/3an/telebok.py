import tkinter as tk
import tkinter.messagebox as msg 

class Person:
    def __init__(self, namn, tele):
        self.namn = namn
        self.tele = tele

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.persons = []
        self.wm_title("Telefonbok")

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

class Start(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="välkommen till telefonboken")
        label.pack(pady=10, padx=10)

        buttonAdd = tk.Button(self, text="Lägg in en person", command=lambda: controller.show_frame(Add))
        buttonAdd.pack()

        buttonShow = tk.Button(self, text="visa alla personer", command=lambda: controller.show_frame(Show))
        buttonShow.pack()

        buttonQuit = tk.Button(self, text="Avsluta", command=lambda: controller.quit())
        buttonQuit.pack()

class Add(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        nameLabel = tk.Label(self, text="Namn: ")
        nameLabel.grid(row=0, column=0)

        teleLabel = tk.Label(self,text="Telenr: ")
        teleLabel.grid(row=1, column=0)

        self.nameEntry = tk.Entry(self)
        self.nameEntry.grid(row=0, column=1)
        
        self.teleEntry = tk.Entry(self)
        self.teleEntry.grid(row=1, column=1)

        buttonSave = tk.Button(self, text="Spara", command=self.save)
        buttonSave.grid(row=2, column=0, columnspan=2)

        buttonBack = tk.Button(self, text="Tillbaka", command=lambda: self.controller.show_frame(Start))
        buttonBack.grid(row=3, column=0, columnspan=2)

    def save(self):
        name = self.nameEntry.get()
        tele = self.teleEntry.get()

        self.controller.persons.append(Person(name, tele))

class Show(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.build(parent, controller)

    def build(self, parent, controller):
        label = tk.Label(self, text="Här är alla personer")
        label.pack(pady=10, padx=10)

        for person in controller.persons:
            label = tk.Label(self, text="{} {}".format(person.namn, person.tele))
            label.pack()

        buttonBack = tk.Button(self, text="Tillbaka", command=lambda: controller.show_frame(Start))
        buttonBack.pack()

    def update(self, parent, controller):
        for widget in self.winfo_children():
            widget.destroy()

        self.build(parent, controller)

if __name__ == "__main__":
    W = Window()
    W.mainloop()