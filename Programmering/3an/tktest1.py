from tkinter import *

class Main():
    def __init__(self, root):
        self.root = root

        self.aLabel = Label(self.root, text="Lite stuff")
        self.aLabel.pack()

        self.aButton = Button(self.root, text="En Meningslös knapp")
        self.aButton.pack()

        self.bLabel = Label(self.root, text="WÖÖÖÖÖÖÖÖW")
        self.bLabel.pack()


if __name__ == "__main__":
    root = Tk()
    Main(root)
    root.mainloop()