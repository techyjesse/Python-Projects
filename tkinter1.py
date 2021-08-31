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
        self.master.config(bg='darkgray')

        self.varFname = StringVar()
        self.varLname = StringVar()

        self.lblFname = Label(self.master,text='First Name: ', font= ("Helvetica", 16), fg='black',bg='lightblue')
        self.lblFname.grid(row=0,column=0)

        self.lblLname = Label(self.master,text='Last Name: ', font= ("Helvetica", 16), fg='black',bg='lightblue')
        self.lblLname.grid(row=1,column=0)
        

        self.txtFname = Entry(self.master,text=self.varFname, font= ("Helvetica", 16), fg='black',bg='lightblue')
        self.txtFname.grid(row=,column=)

        self.txtLname = Entry(self.master,text=self.varLname, font= ("Helvetica", 16), fg='black',bg='lightblue')
        self.txtLname.grid(row=,column=)











if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    # keeps program functioning and open
    root.mainloop()
