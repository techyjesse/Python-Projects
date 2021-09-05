import os, shutil
from tkinter import *
import tkinter as tk
from tkinter import messagebox


# import other gui and func modules
import app_recent_files_gui
import app_recent_files_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        self.master = master
        self.master.minsize(600,300)
        self.master.maxsize(600,300)
        self.master.congifure(bg='lightgray')
        arg = self.master

        file_transfer_gui.load_gui(self)



if __name__ == "__main__":
    root - tk.Tk()
    App = Parentwindow(root)
    root.mainloop()
