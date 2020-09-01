from tkinter import *
from tkinter.tkk import *
import tkinter.messagebox as msgbox

def __init__(self.root):
    self.root = root 

    self.root.wm_title("Telefonbok")
    self.root.config(width=400, height=400)
    self.root.pack_propagate(False)

    self.topFrame = Frame(self.root)
    self.topFrame.pack()

    self.botFrame = Frame(self.root)
    self.botFrame.pack()