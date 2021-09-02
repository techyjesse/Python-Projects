import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,400))
        # title of UGI displays in top bar
        self.master.title('Learning Tkinter!')
        # sets background color to UGI
        self.master.config(bg='lightgray')

        self.varFname = StringVar()
        self.varLname = StringVar()
        # label boxes placed to left of GUI
        self.lblFname = Label(self.master,text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblFname.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblLname = Label(self.master,text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblLname.grid(row=1, column=0, padx=(30,0), pady=(30,0))
        
        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))
        # display box for user input First Name
        self.txtFname = Entry(self.master,text=self.varFname, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFname.grid(row=0, column=1, padx=(30,0), pady=(30,0))
        # display box for user input Last Name
        self.txtLname = Entry(self.master,text=self.varLname, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLname.grid(row=1, column=1, padx=(30,0), pady=(30,0))
        # submit button
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)
        # cancel button
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)
    # function for submit button
    def submit(self):
        fn = self.varFname.get()
        ln = self.varLname.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))
    # function for cancel button / exits GUI
    def cancel(self):
        self.master.destroy()
        
        

       











if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    # keeps program functioning and open
    root.mainloop()
