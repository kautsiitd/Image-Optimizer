from Tkinter import *
from ttk import Style, Label
import tkFileDialog
# own files
from main import *
from my_globals import my_globals as gbl
import size_reduce

class reducer_window(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)    
		self.parent = parent
		parent.style=Style    ()
		parent.style.theme_use("classic")
		self.initUI           (parent)
		
	def initUI(self,parent):
		Style().configure("TLabel", font='serif 10', expand='True')
		menubar = Menu(self.parent)
		self.parent.config(menu=menubar)

		# creating window structure
		parent.rowconfigure    (0, weight=1, pad=5)
		parent.rowconfigure    (1, weight=1, pad=5)
		for i in range(2,18):
			parent.rowconfigure(i, weight=0, pad=5)
		parent.columnconfigure (0, weight=0, pad=5)
		parent.columnconfigure (1, weight=1, pad=5)
		parent.columnconfigure (2, weight=1, pad=5)

		# creating advance menu
		advance_menu = Menu(menubar)
		advance_menu.add_command(label="Resolution"         )
		advance_menu.add_command(label="Other"           	)
		# adding menus to menubar
		menubar.add_cascade(label="Advance_Settings"             , menu=advance_menu)
		
		# track for entry widgets
		self.e1s = StringVar(parent)
		self.e2s = StringVar(parent)
		self.e3s = StringVar(parent)
		self.e4s = StringVar(parent)
		self.e5s = StringVar(parent)
		self.e6s = StringVar(parent)
		self.e7s = StringVar(parent)
		self.e8s = StringVar(parent)
		self.e9s = StringVar(parent)
		self.e10s= StringVar(parent)

		self.e1s .trace("w", self.check)
		self.e2s .trace("w", self.check)
		self.e3s .trace("w", self.check)
		self.e4s .trace("w", self.check)
		self.e5s .trace("w", self.check)
		self.e6s .trace("w", self.check)
		self.e7s .trace("w", self.check)
		self.e8s .trace("w", self.check)
		self.e9s .trace("w", lambda name, idx, mode:self.check("width_edit" ))
		self.e10s.trace("w", lambda name, idx, mode:self.check("height_edit"))

		# creating entry widget
		self.e1 = self.create_entry(self.e1s , 0, 1, 2, "news", "" 	   )
		self.e2 = self.create_entry(self.e2s , 1, 1, 2, "news", "" 	   )
		self.e3 = self.create_entry(self.e3s , 2, 1, 2, "ew"  , 50 	   )
		self.e4 = self.create_entry(self.e4s , 4, 1, 2, "ew"  , 200	   )
		self.e5 = self.create_entry(self.e5s , 6, 1, 2, "ew"  , 85 	   )
		self.e6 = self.create_entry(self.e6s , 8, 1, 2, "ew"  , 90 	   )
		self.e7 = self.create_entry(self.e7s ,10, 1, 2, "ew"  , 95 	   )
		self.e8 = self.create_entry(self.e8s ,12, 1, 2, "ew"  , "JPEG" )
		self.e9 = self.create_entry(self.e9s ,14, 1, 1, "ew"  , 600	   )
		self.e10= self.create_entry(self.e10s,14, 2, 1, "ew"  , "A/c w")

		# creating buttons
		self.ib = self.create_button("Input Directory"   ,"active"  , self.Open_i_Directory, 0, 0, 1, 5)
		self.ib.bind('<Return>', self.Open_i_Directory)
		self.ob = self.create_button("Output Directory"  ,"active"  , self.Open_o_Directory, 1, 0, 1, 5)
		self.ob.bind('<Return>', self.Open_o_Directory)
		self.ex = self.create_button("Exit"              ,"active"  , self.do_exit         ,17, 0, 1, 5)
		self.ex.bind('<Return>', self.do_exit)
		self.b1 = self.create_button("Compress"          ,"disabled", self.go_compress     ,17, 2, 1, 5)
		self.b1.bind('<Return>', self.go_compress)
		self.b2 = self.create_button("Default"           ,"active"  , self.default         ,17, 1, 1, 5)
		self.b2.bind('<Return>', self.default)

		# creating Lables
		self.create_label("Min_Memory"   , 2, 0)
		self.create_label("(KB)"         , 3, 2)
		self.create_label("Max_Memory"   , 4, 0)
		self.create_label("(KB)"         , 5, 2)
		self.create_label("Min_Quality"  , 6, 0)
		self.create_label("[1-100]"      , 7, 2)
		self.create_label("Base_Quality" , 8, 0)
		self.create_label("B/W Min & Max", 9, 2)
		self.create_label("Max_Quality"  ,10, 0)
		self.create_label("[1-100]"      ,11, 2)
		self.create_label("Format"       ,12, 0)
		self.create_label("JPEG & PNG"   ,13, 2)
		self.create_label("Resolution"   ,14, 0)
		self.create_label("width"   	 ,15, 1)
		self.create_label("height"   	 ,15, 2)

		# creating check buttons
			# creating variable for check button
		self.crop= IntVar()
		self.optm= IntVar()
		self.enc = IntVar()
			# creating check buttons
		self.optimize = Checkbutton(parent, text="Optimize"   , font='serif 10',variable=self.optm, command=self.optmClick)
		self.c_crop   = Checkbutton(parent, text="Center_Crop", font='serif 10',variable=self.crop, command=self.cropClick)
		self.encode   = Checkbutton(parent, text="Encode"     , font='serif 10',variable=self.enc , command=self.enClick  )
			# placing checkbuttons
		self.optimize.grid(row = 16, column = 0)
		self.c_crop  .grid(row = 16, column = 1)
		self.encode  .grid(row = 16, column = 2)
			# already selected
		self.optimize.select()
		self.encode  .select()

		# filling text
		self.default()
		
	def optmClick(self):
		if self.optm.get() == 1:
			gbl.do_optimize = 1
		else:
			gbl.do_optimize = 0

	def cropClick(self):
		if self.crop.get() == 1:
			gbl.do_c_crop   = 1
		else:
			gbl.do_c_crop   = 0
			if  (self.e9 .get().isdigit()):
				self.e10 .delete(0, "end")
				self.e10 .insert(0, "A/c w")
			elif(self.e10.get().isdigit()):
				self .e9 .delete(0, "end")
				self .e9 .insert(0, "A/c h")

	def enClick(self):
		if self.enc.get() == 1:
			gbl.do_encode =  1
		else:
			gbl.do_encode =  0

	def do_exit (self, *args):
		self.quit()

	def create_button(self, text_, state_, command_, row_, column_, columnspan_, pad_):
		temp = Button(self.parent, text=text_, state=state_, font='serif 10', command=command_)
		temp.grid(row=row_, column=column_, columnspan=columnspan_, sticky='ew', padx= pad_, pady=4)
		return temp

	def create_entry(self, text_var, row_no, column_no, columnspan_, sticky_, text_):
		temp_entry = Entry(self.parent, text=str(text_), textvariable=text_var, font='serif 10', bg="white", bd=4, cursor="xterm", fg="Black", justify="center", relief="ridge")
		temp_entry.grid(row=row_no, column=column_no, columnspan=columnspan_, sticky=sticky_, padx=5)
		return temp_entry

	def create_label(self, text_, row_, column_):
		Label(self.parent, text=text_, anchor="nw", font='serif 10').grid(row=row_, column=column_)

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
			print "input_dir",gbl.input_dir

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

	def check(self, *args):
		# correcting resolution if do not center crop
		if(gbl.do_c_crop == 0):
			if  (self.e9 .get().isdigit() and args[0] == "width_edit" ):
				self.e10 .delete(0, "end")
				self.e10 .insert(0, "A/c w")
			elif(self.e10.get().isdigit() and args[0] == "height_edit"):
				self .e9 .delete(0, "end")
				self .e9 .insert(0, "A/c h")
		# getting data
		e1_data =self.e1s .get()
		e2_data =self.e2s .get()
		e3_data =self.e3s .get()
		e4_data =self.e4s .get()
		e5_data =self.e5s .get()
		e6_data =self.e6s .get()
		e7_data =self.e7s .get()
		e8_data =self.e8s .get()
		e9_data =self.e9s .get()
		e10_data=self.e10s.get()
		# checking data
		c1 = e1_data
		c2 = e2_data
		c3 = e3_data.isdigit () and 0<e3_data
		c4 = e4_data.isdigit () and 0<e4_data
		c5 = e5_data.isdigit () and 0<int(e5_data)<101
		c6 = e5_data.isdigit () and e6_data.isdigit() and e7_data.isdigit() and int(e5_data)<=int(e6_data)<=int(e7_data)
		c7 = e7_data.isdigit () and 0<int(e7_data)<101
		c8 = 0
		c9 = e9_data.isdigit () and 0<int(e9_data )
		c10= e10_data.isdigit() and 0<int(e10_data)
		c11= 0
		if  (gbl.do_c_crop == 0 and c9  and e10_data == "A/c w"):
			c11 = 1
		elif(gbl.do_c_crop == 0 and c10 and e9_data  == "A/c h"):
			c11 = 1
		if e8_data in ["JPEG" ,"PNG"]: c8 = 1
		if c1 and c2 and c3 and c4 and c5 and c6 and c7 and c8 and ((c9 and c10) or c11):
			self.b1    .config(state="active")
			self.b1    .bind('<Return>', self.go_compress)
			self.parent.bind('<Return>', self.go_compress)
			gbl.input_dir = e1_data
			gbl.output_dir= e2_data
			gbl.min_m 	  = int(e3_data  )
			gbl.max_m 	  = int(e4_data  )
			gbl.min_q 	  = int(e5_data  )
			gbl.bse_q 	  = int(e6_data  )
			gbl.max_q 	  = int(e7_data  )
			gbl.form	  = 	e8_data  
			gbl.width 	  = 	e9_data
			gbl.height 	  = 	e10_data
		else:
			self.b1    .config(state="disabled")
			self.b1    .unbind('<Return>')
			self.parent.unbind('<Return>')

	def go_compress(self, *args):
		size_reduce.size_reduce()
		self.quit()

	def default(self, *args):
		self.e3 .delete(0, "end" )
		self.e4 .delete(0, "end" )
		self.e5 .delete(0, "end" )
		self.e6 .delete(0, "end" )
		self.e7 .delete(0, "end" )
		self.e8 .delete(0, "end" )
		self.e3 .insert(0,50	 )
		self.e4 .insert(0,200	 )
		self.e5 .insert(0,85	 )
		self.e6 .insert(0,90	 )
		self.e7 .insert(0,95	 )
		self.e8 .insert(0,"JPEG" )
		self.e9 .delete(0, "end" )
		self.e9 .insert(0,600	 )
		self.e10.delete(0, "end" )
		self.e10.insert(0,"A/c w")
		self.optimize.select()
		self.c_crop.deselect()
		self.encode  .select()