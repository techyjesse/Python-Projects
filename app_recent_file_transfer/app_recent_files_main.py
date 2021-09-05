import os, shutil
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time


# import other gui and func modules
import app_recent_files_gui
import app_recent_files_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(800,500)
        self.master.maxsize(800,500)
        self.master.config(bg='lightblue')
        arg = self.master

        app_recent_files_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
