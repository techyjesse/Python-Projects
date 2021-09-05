import os, shutil, sqlite3
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter as tk
import time

# import other modules
import app_recent_files_main
import app_recent_files_gui

def browseFile1(self):
    directory = filedialog.askdirectory()
    #clears content for directory
    self.txt_file1.delete(0,END)
    #populates directory
    self.txt_file1.insert(END,directory) 

def browseFile2(self):
    directory = filedialog.askdirectory()
    #clears content for directory
    self.txt_file2.delete(0,END)
    #populates directory
    self.txt_file2.insert(END,directory) 

def transferFiles(self):
    self.lbl_success.config(text="") 
    source = self.txt_file1.get()
    destination = self.txt_file2.get()
    # require user to select both fields in entry boxes
    if (len(source) > 0) and (len(destination) > 0):
        if source != destination:
            source = source + "/" 
            destination = destination + "/"
            files = os.listdir(source)
            fileNames = "" 
            for i in files:
                #checks mod time to see if file meets criteria
                if checkModTime(source,i): 
                    fileNames = fileNames + i + "\n"
            if (len(fileNames) > 0):
                askToMove = messagebox.askokcancel("Ok to move?","Files available to move:\n\n{}\nDo you wish to continue?".format(fileNames))
                if askToMove:
                    for i in files:
                        if checkModTime(source,i):
                            shutil.move(source+i, destination)
                    self.lbl_success.config(text="Your files have transferred successfully.")
            else:
                messagebox.showerror("No files have currently been modified in the last 24 hours.")
                self.lbl_success.config(text="No recently edited files in this folder")


def checkModTime(source,file):
    # file path
    path = source + file
    # get modification time
    modTime = os.path.getmtime(path)
    #current time
    curTime = time.time()
    # if else to see if any files have been modified in the last 24 hours
    if (curTime - modTime) / 3600 < 24: 
        return True
    else:
        return False

def ask_quit(self): 
    if messagebox.askokcancel("Exit App", "Okay to exit application?"):
        #close app
        self.master.destroy()
        os.exit(0) 

if __name__ == "__main__":
    pass    
