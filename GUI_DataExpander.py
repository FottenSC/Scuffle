import json
import os
from pathlib import Path
import re
import struct
from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkf
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import MovelistParser
import ConfigReader
import time
from threading import Thread



class GUI_DataExpander:
    def __init__(self, master:Tk, movelist:MovelistParser.Movelist=None):
        self.master = master
        self.movelist = movelist
        master.title('SCUFFLE Data Expander')
        master.iconbitmap(default='Data/icon.ico')
        master.geometry('800x850')
        self.frame = Label(master,text="TEST")
        self.frame.grid()
        self.working_movelist = self.movelist

        #Add Moves (Mode 0)
        move_frame = Frame(master)
        val = StringVar()
        
        move_quantity = Spinbox(move_frame,from_=0, to=20, textvariable=val, width=6, validate='all')

        move_frame.grid(row=0, column=0)
        move_quantity.grid()
        
        #Add Attacks (Mode 1)

        #Add Throws (Mode 2)

        #Add Modifiers (Mode 3)










if __name__ == '__main__':
    root = Tk()
    my_gui = GUI_DataExpander(root)
    root.mainloop()