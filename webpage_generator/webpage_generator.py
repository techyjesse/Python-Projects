
#   Tkinter GUI / Web Page Generator
#   Author : Jesse Kuykendall
#   Python 3.9.7


import tkinter
from tkinter import *
# this module is needed to display webpages
import webbrowser 


# Main window and parent class
class ParentWindow(Frame): 
    def __init__(self, master): 
        Frame.__init__(self)

        # The displayed GUI:
        self.master = master
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.resizable(width=True, height=True)
        self.master.title('Webpage Text Generator')
        self.master.config(bg='lightgrey')

        # Label displaying text
        self.lbl = Label(self.master, text="To update your \nwebpage's body content, \ntype your new \ncontent and click \n submit.")
        self.lbl.place(x=7, y=15, width=175, height=300) # Uniform padding seperates widget from its neighbors
        
        # Multi-line text box
        self.txtbx = Text(self.master, tabs=('.5c'))
        # position and size of text box
        self.txtbx.place(x=190, y=15, width=505, height=300) 
        
        # Submit button
        self.btn_Submit = Button(self.master, width=7, height=1, text="Submit", command=lambda: pageGenerator(self))
        self.btn_Submit.place(x=275,y=335,width=150, height =40)

# Script that generates the webpage:
def pageGenerator(self):
    # captures new text input from textbox 
    newContent = self.txtbx.get('1.0', 'end-1c') 
    fileName = open("newfile.html", "w") 
    fileName.write("<html>\n\t<body>\n\t\t<h3>\n\t{}\n\t\t</h3>\n\t</body>\n</html>".format(newContent)) 
    fileName.close()
    webbrowser.open_new_tab('newfile.html') 
            
if __name__ == '__main__':
    root = Tk() 
    App = ParentWindow(root)
    root.mainloop() 
