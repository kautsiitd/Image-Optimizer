from subprocess import call

from Tkinter import *
from ttk import Style, Label, Scale
import tkFileDialog
from boto.s3.connection import *
# own files
from main import *
from my_globals import my_globals as gbl
import s3_window

class upload_window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)    
        self.parent = parent
        parent.style=Style    ()
        parent.style.theme_use("classic")
        self.initUI           (parent)
        
    def initUI(self,parent):
        Style().configure("TLabel", font='serif 10', expand='True')

        # creating window structure
        parent.columnconfigure(0, weight=0, pad=5)
        parent.columnconfigure(1, weight=1, pad=5)
        parent.columnconfigure(2, weight=0, pad=5)
        parent.rowconfigure   (0, weight=1, pad=5)
        parent.rowconfigure   (1, weight=1, pad=5)
        parent.rowconfigure   (2, weight=0, pad=5)

        # creating buttons
        self.b1     = Button  (self.parent, text="From:"   , command= self.upld_dir,           state="active", font='serif 10')
        self.b1.grid          (row = 0    , column = 0     , padx   = 5)
        self.b1.bind          ('<Return>'                  ,          self.upld_dir)
        self.b2     = Button  (self.parent, text=" To: "   , command= self.to_s3_dir,            state="active", font='serif 10')
        self.b2.grid          (row = 1    , column = 0     , padx   = 5           , sticky = "ew")
        self.b2.bind          ('<Return>'                  ,          self.to_s3_dir)
        self.b3     = Button  (self.parent, text="Exit"    , command= self.do_exit, width  = 3, state="active", font='serif 10')
        self.b3.grid          (row = 2    , column = 0     , padx   = 5           , sticky = "ew")
        self.b3.bind          ('<Return>'                  ,          self.do_exit)
        self.b4     = Button  (self.parent, text="Upload", command= self.s3_upld,            state="active", font='serif 10')
        self.b4.grid          (row = 2    , column = 2     , padx   = 5           , sticky = "ew")
        self.b4.bind          ('<Return>'                  ,          self.s3_upld)

        # creating output entry widget
        self.e1     = Entry   (self.parent, bg="white", bd = 4, cursor = "xterm", fg = "Black", justify = "center", relief = "ridge")
        self.e1.grid          (row = 0, column = 1, columnspan = 2, pady   = 5      ,sticky = "news")
        self.e2     = Entry   (self.parent, bg="white", bd = 4, cursor = "xterm", fg = "Black", justify = "center", relief = "ridge")
        self.e2.grid          (row = 1, column = 1, columnspan = 2, pady   = 5      ,sticky = "news")

    def upld_dir(self, *args):
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = self.parent
        options['title'] = 'Upload_From Directory'
        dr = tkFileDialog.askdirectory(**self.dir_opt)
        if dr != '':
            text = str(dr)
            self.e1.delete(0, 'end')
            self.e1.insert(0, text)
            gbl.dwld_output_dir = text

    def to_s3_dir(self, *args):
        s3 = Toplevel()
        s3.geometry("500x300+400+200")
        s3.title   ("s3_File_selection")
        s3_window.s3_window(s3)
        s3.mainloop()
        s3.destroy ()
        if(gbl.dir_adrs != ""):
            self.e2.delete(0, 'end')
            self.e2.insert(0, gbl.dir_adrs)

    def do_exit (self, *args):
        self.quit()

    def s3_upld (self, *args):
        call("aws s3 sync "+str(self.e1.get())+" "+str(self.e2.get()), shell = True)
        self.quit()