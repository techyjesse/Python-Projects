import os, shutil
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time



#import main and func modules
import app_recent_files_main
import app_recent_files_func


def load_gui(self):

    self.lbl_title = tk.Label(self.master, text="Search & Transfer Recently Edited Files", font=('TkDefaultFont',16))
    self.lbl_title.grid(row=0,column=1,padx=(15,0),pady=(20,10),sticky=N)

    # Folder choice labels
    self.lbl_source = tk.Label(self.master, text="Choose Your Source Folder: ")
    self.lbl_source.grid(row=1,column=0,padx=(10,10),pady=(0,0),sticky=W)
    self.lbl_destination = tk.Label(self.master, text="Choose Your Destination Folder: ")
    self.lbl_destination.grid(row=2,column=0,padx=(10,10),pady=(0,0),sticky=W)

    # success text display
    self.lbl_success = tk.Label(self.master, text="", font=('TkDefaultFont',14))
    self.lbl_success.grid(row=4,column=1,padx=(10,0),pady=(20,10),sticky=W)

    # Browse buttons
    self.btn_browse1 = tk.Button(self.master,width=14,height=1,text="Browse",command=lambda: app_recent_files_func.browseFile1(self))
    self.btn_browse1.grid(row=1,column=2,padx=(10,0),pady=(10,10),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=14,height=1,text="Browse",command=lambda: app_recent_files_func.browseFile2(self))
    self.btn_browse2.grid(row=2,column=2,padx=(10,0),pady=(10,10),sticky=W)
    self.btn_check = tk.Button(self.master,width=22,height=2,text="Check for recently edited files",command=lambda: app_recent_files_func.transferFiles(self))
    self.btn_check.grid(row=3,column=1,padx=(0,10),pady=(25,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=14,height=2,text="Close Application",command=lambda: app_recent_files_func.ask_quit(self))
    self.btn_close.grid(row=3,column=1,padx=(10,10),pady=(25,10),sticky=E)

    # Entry fields
    self.txt_file1 = tk.Entry(self.master,text="",width=40)
    self.txt_file1.grid(row=1, column=0, columnspan=4, padx=(0,0),pady=(10,10))
    self.txt_file2 = tk.Entry(self.master,text="",width=40)
    self.txt_file2.grid(row=2, column=0, columnspan=4, padx=(0,0),pady=(10,10))

    

if __name__ == "__main__":
    pass
