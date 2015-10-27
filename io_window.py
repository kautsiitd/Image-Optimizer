from Tkinter import *
from ttk import Style, Label, Scale
import tkFileDialog
# own files
from main import *
from my_globals import my_globals as gbl
from hover import hover_message

class io_window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)    
        self.parent = parent
        parent.style=Style()
        parent.style.theme_use("classic")
        self.initUI(parent)
        
    def initUI(self,parent):
        Style().configure("TLabel", font='serif 10', expand='True')

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        # creating filemenu
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Input File"      , command=self.Open_File)
        fileMenu.add_separator()
        fileMenu.add_command(label="Input Directory" , command=self.Open_i_Directory)
        fileMenu.add_command(label="Output Directory", command=self.Open_o_Directory)
        # creating s3_bucket menu
        s3_menu = Menu(menubar)
        s3_menu.add_command(label="Download"         , command=self.download)
        s3_menu.add_command(label="Upload"           , command=self.upload)
        # creating option menu
        opt_menu = Menu(menubar)
        opt_menu.add_command(label="Size Reducer"    , command=self.size_reducer)
        # adding menus to menubar
        menubar.add_cascade(label="Open"             , menu=fileMenu)
        menubar.add_cascade(label="S3_Bucket"        , menu=s3_menu )
        menubar.add_cascade(label="Other"            , menu=opt_menu)

        # track for entry in i/o entry widgets
        self.e1s = StringVar(parent)
        self.e2s = StringVar(parent)

        self.e1s.trace("w", self.check)
        self.e2s.trace("w", self.check)

        # creating frame
        parent.columnconfigure(0, weight=0, pad=5)
        parent.columnconfigure(1, weight=1, pad=5)
        parent.columnconfigure(2, weight=1, pad=5)
        parent.rowconfigure	  (0, weight=1, pad=5)
        parent.rowconfigure	  (1, weight=1, pad=5)
        parent.rowconfigure	  (2, weight=0, pad=5)

        # creating i/o Buttons
        self.ib = self.create_button("Input Directory"	 ,"active", self.Open_i_Directory, 0, 0, 1, 5)
        self.ib.bind('<Return>', self.Open_i_Directory)
        self.ob = self.create_button("Output Directory"	 ,"active", self.Open_o_Directory, 1, 0, 1, 5)
        self.ob.bind('<Return>', self.Open_o_Directory)

        # creating Directory i/o entries widget
        self.e1 = self.create_entry(self.e1s, 0, 1)
        self.e2 = self.create_entry(self.e2s, 1, 1)
        
        # creating next and last_start and exit button
        self.b1 = self.create_button("Next>>"	 , "disabled", self.go_next, 2, 2, 1, 5)
        self.b1.bind('<Return>', self.go_next)
        self.b2 = self.create_button("Exit"	 	 , "active"	 , self.do_exit, 2, 0, 1, 5)
        self.b2.bind('<Return>', self.do_exit)
        self.b3 = self.create_button("From Last", "active"	 , self.go_last, 2, 1, 1, 5)
        self.b3.bind('<Return>', self.go_last)

        # Display messages
        hover_message(self.ib, text = "Choose Input directory which you want to compress")
        hover_message(self.ob, text = "Choose Output directory where you want to save compressed photos")
        hover_message(self.b1, text = "Compress Images manually")
        hover_message(self.b2, text = "Quit")
        hover_message(self.b3, text = "Start from where you left")
    
    def size_reducer(self, *args):
        gbl.size_reducer = 1
        self.quit()

    def download(self, *args):
        gbl.download_prsd = 1
        self.quit()

    def upload(self, *args):
        gbl.upload_prsd = 1
        self.quit()

    def create_entry(self, text_var, row_no, column_no):
        temp_entry = Entry(self.parent, textvariable=text_var, font='serif 10', bg="white", bd=4, cursor="xterm", fg="Black", justify="center", relief="ridge")
        temp_entry.grid(row=row_no, column=column_no, columnspan=2, sticky="ew", padx=5)
        return temp_entry

    def create_button(self, text_, state_, command_, row_, column_, columnspan_, pad_):
        temp = Button(self.parent, text=text_, state=state_, font='serif 10', command=command_)
        temp.grid(row=row_, column=column_, columnspan=columnspan_, sticky='ew', padx= pad_, pady=4)
        return temp
    
    def check(self, *args):
        e1_data=self.e1s.get()
        e2_data=self.e2s.get()
        if e1_data and e2_data:
            self.b1.config(state="active")
            self.b1    .bind('<Return>', self.go_next)
            self.parent.bind('<Return>', self.go_next)
            gbl.input_dir=e1_data
            gbl.output_dir=e2_data
        else:
            self.b1.config(state="disabled")
            self.b1    .unbind('<Return>')
            self.parent.unbind('<Return>')
    
    def go_next(self, *args):
        self.quit()

    def do_exit(self, *args):
        gbl.exit = 1
        self.quit()

    def go_last(self, *args):
        gbl.last_start = 1
        self.quit()

    def Open_File(self):
      	ftypes = [('Image files', '*.PNG'),('Image files', '*.JPEG'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        if fl != '':
            text = str(fl)
            self.e1.delete(0, 'end')
            self.e1.insert(0, text)
            gbl.input_dir = text

    def Open_i_Directory(self):
    	self.dir_opt = options = {}
    	options['initialdir'] = 'C:\\'
    	options['mustexist'] = False
    	options['parent'] = self.parent
    	options['title'] = 'Input Directory'
    	dr = tkFileDialog.askdirectory(**self.dir_opt)
    	if dr != '':
            text = str(dr)
            self.e1.delete(0, 'end')
            self.e1.insert(0, text)
            gbl.input_dir = text

    def Open_o_Directory(self):
		self.dir_opt = options = {}
		options['initialdir'] = 'C:\\'
		options['mustexist'] = False
		options['parent'] = self.parent
		options['title'] = 'Output Directory'
		dr = tkFileDialog.askdirectory(**self.dir_opt)
		if dr != '':
			text = str(dr)
			self.e2.delete(0, 'end')
			self.e2.insert(0, text)
			gbl.output_dir = text

    def readFile(self, filename):
        f = open(filename, "r")
        text = f.read()
        return text