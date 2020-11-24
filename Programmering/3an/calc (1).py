#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
<PROGRAMNAMN>
Namn: Christian Fröberg
Datum: 2018-01-03
Beskrivning:

En väldigt enkel kalkylator

"""
import tkinter as tk

class Calculator:
    def __init__(self, root):
        # Instansvariabler
        self.root = root
        self.displayFrame = tk.Frame(self.root)
        self.buttonsFrame = tk.Frame(self.root)
        self.optFrame = tk.Frame(self.root)
        self.textDisplay = tk.Entry(self.displayFrame)

        # Bygger fönstret
        self.root.wm_title("En enkel kalkylator")
        self.root.resizable(width=False, height=False)
        self.buildframes()
        self.buildnobuttons()
        self.buildoptbuttons()
        self.builddisplay()

    def buildframes(self):
        self.displayFrame.config(height=50, width=400)
        self.displayFrame.pack_propagate(False)
        self.displayFrame.pack()

        self.buttonsFrame.config(height=400, width=100)
        self.buttonsFrame.pack_propagate(False)
        self.buttonsFrame.pack(anchor="s", side="left")

        self.optFrame.config(height=400, width=100)
        self.optFrame.pack()

    def buildnobuttons(self):
        var = 1
        for x in range(3):
            for y in range(3):
                button = tk.Button(self.buttonsFrame, text=var, height=5, width=12)
                button.grid(row=x, column=y, pady=2, padx=2)
                button.bind("<Button-1>", self.buttonclicked)
                var += 1

    def buildoptbuttons(self):
        button = tk.Button(self.optFrame, text="C", height=5, width=12)
        button.bind("<Button-1>", self.buttonclicked)
        button.pack(pady=2, padx=2)

        button = tk.Button(self.optFrame, text="+", height=5, width=12)
        button.bind("<Button-1>", self.buttonclicked)
        button.pack(pady=2, padx=2)

        button = tk.Button(self.optFrame, text="-", height=5, width=12)
        button.bind("<Button-1>", self.buttonclicked)
        button.pack(pady=2, padx=2)

        button = tk.Button(self.optFrame, text="=", height=5, width=12)
        button.bind("<Button-1>", self.buttonclicked)
        button.pack(pady=2, padx=2)


    def builddisplay(self):
        self.textDisplay.config(justify="right", width=50)
        self.textDisplay.place(x=50, y=17)
        

    def buttonclicked(self, event):
        pass


if __name__ == '__main__':
    window = tk.Tk()
    Calculator(window)
    window.mainloop()