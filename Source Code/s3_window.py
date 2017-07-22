from Tkinter import *
from ttk import Style, Label, Scale
import tkFileDialog
from boto.s3.connection import *
from boto.s3.key import Key
# own files
from my_globals import my_globals as gbl

# access id and key
AWS_KEY 		= '*************'
AWS_SECRET 		= '*************'

# making connection
aws_connection  = S3Connection(AWS_KEY, AWS_SECRET)

class s3_window():
    def __init__(self, parent):
        self.parent = parent
        parent.style=Style 	  ()
        parent.style.theme_use("classic")
        self.initUI			  (parent)
        
    def initUI(self,parent):
        # resetting variables
        gbl.level = 0

        Style().configure("TLabel", font='serif 10', expand='True')

        # creating window structure
        parent.columnconfigure(0, weight=0, pad=5)
        parent.columnconfigure(1, weight=1, pad=5)
        parent.columnconfigure(2, weight=1, pad=5)
        parent.columnconfigure(3, weight=1, pad=5)
        parent.columnconfigure(4, weight=0, pad=0)
        parent.columnconfigure(5, weight=0, pad=0)
        parent.rowconfigure	  (0, weight=0, pad=5)
        parent.rowconfigure	  (1, weight=1, pad=5)
        parent.rowconfigure	  (2, weight=1, pad=5)
        parent.rowconfigure	  (3, weight=1, pad=5)
        parent.rowconfigure	  (4, weight=0, pad=0)
        parent.rowconfigure	  (5, weight=0, pad=5)
        parent.rowconfigure	  (6, weight=0, pad=5)

        # creating labels
        Label				  (self.parent, text="Directory:"  ).grid(row=0)
        Label				  (self.parent, text=" Selection: ").grid(row=5)

        # creating options menu button
        self.variable = StringVar(parent)
        self.variable.set     ("s3:/") # default value
        self.options  =       ["waste"]
        self.om1 = OptionMenu (parent     , self.variable, *self.options)
        del self.options[-1]
        self.om1['menu'].delete("end")
        # attaching command to first option
        self.prefix = ""
        self.options.append   ("s3:/")
        self.om1['menu'].add_command(label = self.options[-1], command = lambda opt = self.options[-1]: self.flight(opt))
        self.om1.grid		  (row = 0	  , column = 1   , columnspan = 3	   , pady   = 5, sticky = "news")

        # creating buttons
        self.b1 	= Button  (self.parent, text="UP"    , command=self.up_prsd, width  = 3, state="disabled", font='serif 10')
        self.b1.grid		  (row = 0 	  , column = 4)
        self.b1.bind		  ('<Return>' 			     , 		   self.up_prsd)
        self.b2 	= Button  (self.parent, text="OK"    , command=self.ok_prsd, width  = 5, state="active"  , font='serif 10')
        self.b2.grid		  (row = 5 	  , column = 4)
        self.b2.bind		  ('<Return>' 			     , 		   self.do_exit)
        self.b3 	= Button  (self.parent, text="Cancel", command=self.do_exit, width  = 7, state="active"  , font='serif 10')
        self.b3.grid		  (row = 6 	  , column = 4)
        self.b3.bind		  ('<Return>' 			     , 		   self.do_exit)

        # creating list widget
        # getting all buckets
        self.bucket = aws_connection.get_all_buckets()

        self.l1   	= Listbox (self.parent)
        for i in self.bucket:
            self.l1.insert	  (END, i.name)
        self.l1.grid		  (row = 1, column = 0, rowspan    = 3, padx = (5,0), columnspan = 5, sticky = "news")
        # binding list widget to entries to widget
        self.l1.bind('<Double-1>', self.selected)

        # Scrollbars
        # attaching horizontal scrollbar to list widget
        self.xScroll= Scrollbar(self.parent		  , orient 	   = "horizontal"	 )
        self.xScroll.grid	  (row = 4, column = 0, 			    padx = (6,0), columnspan = 5, sticky = "ew")
        self.xScroll 		  ['command'] 	   = self.l1.xview
        self.l1.configure 	  (xscrollcommand  = self.xScroll.set)

		# attaching vertical scrollbar to list widget
        self.yScroll= Scrollbar(self.parent		  , orient 	   = "vertical"	 )
        self.yScroll.grid	  (row = 1, column = 5, rowspan	   = 3, padx = (0,5), pady = 1		, sticky = "ns")
        self.yScroll 		  ['command'] 	   = self.l1.yview
        self.l1.configure 	  (yscrollcommand  = self.yScroll.set)        

        # creating output entry widget
        self.e1 = Entry  (self.parent, bg="white", bd = 4, cursor = "xterm", fg = "Black", justify = "center", relief = "ridge")
        self.e1.grid (row = 5, column = 1, columnspan = 3, pady   = 5		,sticky = "news")

    # jump through option menu
    def flight(self, opt):
        # calculating level
        gbl.level = opt.count('/')-1
        # updating
            # options list
        del self.options[gbl.level+1:]
            # options widget
        self.variable.set(opt)
            # options list in option widget
        self.om1['menu'].delete(gbl.level+1, "end")
            # down entry widget
        self.e1.delete(0, 'end')
        self.e1.insert(0, self.variable.get())
            # prefix
        self.prefix = ""
        temp = self.variable.get().split('/')[3:]
        for i in temp:
            self.prefix += str(i)+"/"
            
        # updating list widget
        if(gbl.level==0):
            # disabling up when at bucket level
            self.b1.configure(state = "disabled")
            # updating list widget to bucket names
            self.l1.delete(0,END)
            for i in self.bucket:
                self.l1.insert    (END, i.name)
        else:
            self.l1.delete(0,END)
            temp_last = ""
            print "level in flight",gbl.level
            for i in gbl.bucket_keys:
                temp_split = i.split('/')
                if(i.startswith(self.prefix) and temp_split[gbl.level-1]!=temp_last):
                    temp_last = temp_split[gbl.level-1]
                    self.l1.insert(END,temp_last)

    # option is selected in list widget
    def selected(self, *args):
        # getting selected value
        value = str(self.l1.get(self.l1.curselection()))
        # updating
            # options list
        self.options.append(self.options[gbl.level]+"/"+value)
            # options widget
        self.variable.set(self.options[-1])
            # options list in option widget
        self.om1['menu'].add_command(label = self.options[-1], command = lambda opt = self.options[-1]: self.flight(opt))
            # down entry widget
        self.e1.delete(0, 'end')
        self.e1.insert(0, self.variable.get())
            # prefix
        if(gbl.level>0):
            self.prefix += value+"/"

        # updating list of keys if choosing bucket
        if(gbl.level == 0):
            print "started connecting"
            gbl.bucket_keys = []
            self.b1.configure(state = "active")
            temp1 = aws_connection.get_bucket(value)
            print "Connection established"
            temp  = temp1.list()
            print "list_generated"
            j=0
            for i in temp:
                j+=1;print j,i.name
                gbl.bucket_keys.append(i.name)
            print "bucket_done"
        gbl.level+=1
        # going inside bucket and updating list widget according to level
        self.l1.delete(0,END)
        temp_last = ""
        for i in gbl.bucket_keys:
            temp_split = i.split('/')
            if(i.startswith(self.prefix) and temp_split[gbl.level-1]!=temp_last):
                temp_last = temp_split[gbl.level-1]
                self.l1.insert(END,temp_last)

    # going up in directory
    def up_prsd(self, *args):
        # updating
            # options list
        del self.options[-1]
            # options widget
        self.variable.set(self.options[-1])
            # options list in option widget
        self.om1['menu'].delete("end")
            # down entry widget
        self.e1.delete(0, 'end')
        self.e1.insert(0, self.variable.get())
            # prefix
        self.prefix = ""
        temp = self.variable.get().split('/')[3:]
        for i in temp:
            self.prefix += str(i)+"/"

        # updating list widget
        gbl.level -= 1
        if(gbl.level==0):
            # disabling up when at bucket level
            self.b1.configure(state = "disabled")
            # updating list widget to bucket names
            self.l1.delete(0,END)
            for i in self.bucket:
                self.l1.insert    (END, i.name)
        else:
            self.l1.delete(0,END)
            temp_last = ""
            for i in gbl.bucket_keys:
                temp_split = i.split('/')
                if(i.startswith(self.prefix) and temp_split[gbl.level-1]!=temp_last):
                    temp_last = temp_split[gbl.level-1]
                    self.l1.insert(END,temp_last)

    def do_exit(self, *args):
        gbl.dir_adrs = ""
        self.parent.quit()

    def ok_prsd(self, *args):
        gbl.dir_adrs = self.e1.get()
        self.parent.quit()
