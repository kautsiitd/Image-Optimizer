from Tkinter import *
from ttk import Style, Label
from PIL import *
from PIL.Image import core as _imaging
import sys
import PIL.ImageFilter
import PIL.ImageTk
# own files
from main import *
from my_globals import my_globals as gbl
# local variables
changed = 0

class Crop_Window(Frame):
  
	def __init__(self, parent):
		Frame.__init__	(self, parent)   
		self.parent = 	(parent)
		self.initUI		(parent)
		
	def initUI(self,parent):
		self.style = Style 	()
		self.style.theme_use("classic")
		Style().configure	("TEntry", font='serif 10')
		Style().configure	("TLabel", font='serif 10')

		# initializing variables
		self.e1s 	  = None
		self.e2s 	  = None
		self.width_e  = None
		self.height_e = None

		# creating menubar
		menubar = Menu(self.parent)
		self.parent.config(menu=menubar)
		
		fileMenu = Menu(menubar)
		fileMenu.add_command(label="Restart", command=self.re_start)
		menubar .add_cascade(label="Options", menu=fileMenu)

		# making frames
		self.frame1=Frame(self.parent 	, relief="sunken")
		self.frame3=Frame(self.frame1 	, relief="sunken")
		self.frame4=Frame(self.frame1 	, relief="sunken")
		self.frame5=Frame(self.parent	, relief="groove")
		self.frame2=Frame(self.parent 	, relief="flat"	 , bg="#333")
		self.frame5.pack (side="bottom"	, fill=X	 	 )
		self.frame1.pack (side="left" 	, fill=Y 		 )
		self.frame2.pack (side="left"	, fill="both"	 , expand="True")
		self.frame3.pack (side="bottom"	, fill=X 		 )
		self.frame4.pack (side="bottom"	, fill=X 		 )

		""" Construction in Frame2 """

		# creating canvas in frame2
		self.canvas = Canvas(self.frame2)
		self.canvas.pack( fill = "both" , expand = "True")

		# blurring and putting back image on canvas
		# b_im = filters.gaussian_filter(gbl.input_im,5)
		self.b_im 	= gbl.input_im.filter(PIL.ImageFilter.BLUR)
		# b_im = gbl.input_im.filter(PIL.ImageFilter.MinFilter(9))
		# b_im = gbl.input_im.filter(PIL.ImageFilter.MaxFilter(5))
		gbl.im 		= PIL.ImageTk.PhotoImage(self.b_im)
		self.im_c 	= self.canvas.create_image( gbl.w/2, gbl.h/2,image = gbl.im)
		
		# cropping and putting focused image on canvas
		cropx,cropy = self.crop_size()
		self.f_im 	= gbl.input_im.crop((cropx, cropy, gbl.w-cropx, gbl.h-cropy))
		gbl.show_im = PIL.ImageTk.PhotoImage(self.f_im)
		gbl.f_im_c 	= self.canvas.create_image(gbl.w/2,gbl.h/2,image = gbl.show_im)

		# creating Rectangle on frame2
		cropx,cropy =self.crop_size()
		self.re1	=self.canvas.create_rectangle(cropx, cropy, gbl.w-cropx, gbl.h-cropy, outline="#333", width=5)
		gbl.x1 		= cropx
		gbl.y1 		= cropy
		gbl.x2 		= gbl.w-cropx
		gbl.y2 		= gbl.h-cropy
		self.canvas.bind		("<Button 1>", self.set_mouse)

		"""Frame 1 construction """

		# creating Next>> button and Exit button
		self.b5 	= Button 	(self.frame3	, text="Exit"  , command=self.do_exit, width=7, 	 state="active", font='serif 10')
		self.b5.pack			(side="left"	, anchor='w'   ,	 padx=4		   , pady=4 )
		self.b5.bind			('<Return>'		, self.do_exit)
		self.b6 	= Button 	(self.frame3	, text="Skip>>", command=self.do_skip, width=7, 	 state="active", font='serif 10')
		self.b6.pack			(side="right"	, anchor='e'   , 	 padx=4		   , pady=4 )
		self.b6.bind			('<Return>'		, self.do_skip)
		self.b7 	= Button 	(self.frame4	, text="<<Back", command=self.go_back, width=7, 	state="active", font='serif 10')
		self.b7.pack			(side="left"	, anchor='center'   , 	padx=4		   , pady=4 )
		self.b7.bind			('<Return>'		, self.go_back)
		self.b4 	= Button 	(self.frame4	, text="Next>>", command=self.do_next, width=7, 	state="active", font='serif 10')
		self.b4.pack			(side="right"	, anchor='center'   , 	padx=4		   , pady=4 )
		self.b4.bind			('<Return>'		, self.do_next)

		# configuring <<back button if cu_ind==0 because cann't go back more
		if(gbl.cu_ind==0):
			self.b7.config(state="disabled")

		# track of width and height entries
		self.e1s 	= StringVar	(self.frame1)
		self.e2s 	= StringVar	(self.frame1)
		self.e1s.trace			("w", lambda name ,idx ,mode:self.check("width_edit" ))
		self.e2s.trace			("w", lambda name ,idx ,mode:self.check("height_edit"))

		# creating check box for keep aspect ratio of image
			# creating variable for check button
		self.keep_ratio= IntVar ()
			# creating check buttons
		keep_aspect_ratio = Checkbutton(self.frame1, text="Keep aspect_ratio"   , font='serif 10', variable=self.keep_ratio, command=self.keep_ratio_Click)

		# creating width and height entries
		self.width_e = Entry	(self.frame1, bg="white", bd=4, cursor="xterm", fg="Black", justify="center", relief="ridge", textvariable=self.e1s)
		self.height_e= Entry	(self.frame1, bg="white", bd=4, cursor="xterm", fg="Black", justify="center", relief="ridge", textvariable=self.e2s)
		self.width_e .insert	(0,gbl.width)
		self.height_e.insert	(0,gbl.height)
		self.width_e .pack		(side="top")
		Label					(self.frame1, text="Width (Default 1080)").pack(side="top")
		self.height_e.pack		(side="top")
		Label					(self.frame1, text="Height (Default 1920)").pack(side="top")
			# placing checkbuttons
		keep_aspect_ratio.pack  (side="top")

		# creating status bar in frame 5
		Label					(self.frame5, text=gbl.input_file) 							  .pack(side="left" , anchor="w")
		Label					(self.frame5, text=str(gbl.cu_ind+1)+"/"+str(gbl.total_files)).pack(side="right", anchor="e")
		
	def keep_ratio_Click(self):
		if self.keep_ratio.get() == 1 and self.width_e!=None and self.height_e!=None:
			if self.e1s.get().isdigit():
				temp = int((int(self.e1s.get())*gbl.h*1.0)/gbl.w)
				self.height_e.delete  (0,'end')
				self.height_e.insert  (0,temp)
			elif self.e2s.get().isdigit():
				temp = int((int(self.e2s.get())*gbl.w*1.0)/gbl.h)
				self.height_e.delete  (0,'end')
				self.height_e.insert  (0,temp)

	def crop_size(self):
		if((gbl.w*1.0)/gbl.h>=(int(gbl.width)*1.0)/int(gbl.height)):
			cropx=((gbl.height*gbl.w)-	(gbl.width*gbl.h))/(gbl.height*2)
			cropy=0
		else:
			cropx=0
			cropy=((gbl.width*gbl.h) -	(gbl.height*gbl.w))/(gbl.width*2)
		return cropx,cropy

	def set_mouse(self, event):
		gbl.mouse_x	 =event.x
		gbl.mouse_y	 =event.y
		if(self.e1s != None and self.e2s != None):
			self.check("no_edit")

	def do_next(self, *args):
		gbl.cu_ind+=1
		self.quit()

	def do_exit(self, *args):
		gbl.exit = 1
		self.quit()

	def do_skip(self, *args):
		gbl.skip = 1
		gbl.cu_ind+=1
		self.quit()	

	def go_back(self, *args):
		gbl.cu_ind-=1
		self.quit()

	def check(self,*args):
		global changed
		if(self.width_e != None and self.height_e != None):
			if(args[0] == "width_edit" and self.e1s.get().isdigit() and self.keep_ratio.get()==1):
				if changed==0:
					changed = 1
					temp = int((int(self.e1s.get())*gbl.h*1.0)/gbl.w)
					self.height_e.delete  (0,'end')
					self.height_e.insert  (0,temp)
				else:
					changed = 0
			elif(args[0] == "height_edit" and self.e2s.get().isdigit() and self.keep_ratio.get()==1):
				if changed==0:
					changed = 1
					temp = int((int(self.e2s.get())*gbl.w*1.0)/gbl.h)
					self.width_e.delete  (0,'end')
					self.width_e.insert  (0,temp)
				else:
					changed = 0
			e1_data		 = self.e1s.get()
			e2_data		 = self.e2s.get()
			if e1_data.isdigit	() and e2_data.isdigit() and int(e1_data)!=0 and int(e2_data)!=0:
				self.b4.config 	(state="active")
				self.parent.bind('<Return>', self.do_next)
				gbl.width 	=int(e1_data)
				gbl.height 	=int(e2_data)
				cropx,cropy =self.crop_size()
				
				shift_x		=0
				shift_y		=0
				if(cropx 	+	(gbl.mouse_x-(gbl.w/2))<0):
					shift_x =abs(cropx+(gbl.mouse_x-(gbl.w/2)))
				if((gbl.w/2)-	 cropx+	gbl.mouse_x	>gbl.w):
					shift_x =	(gbl.w/2)+cropx-gbl.mouse_x
				if(cropy 	+	(gbl.mouse_y-(gbl.h/2))<0):
					shift_y =abs(cropy+(gbl.mouse_y-(gbl.h/2)))
				if((gbl.h/2)-	 cropy+	gbl.mouse_y	>gbl.h):
					shift_y =	(gbl.h/2)+cropy-gbl.mouse_y

				gbl.x1 = cropx+	(gbl.mouse_x-(gbl.w/2))	+shift_x
				gbl.y1 = cropy+	(gbl.mouse_y-(gbl.h/2))	+shift_y
				gbl.x2 = 		(gbl.w/2)	-(cropx) 	+gbl.mouse_x+shift_x
				gbl.y2 = 		(gbl.h/2)	-(cropy) 	+gbl.mouse_y+shift_y

				self.blur 		()
				self.canvas.coords			 (self.re1, gbl.x1, gbl.y1, gbl.x2, gbl.y2)
			else:
				self.b4.config 	  (state="disabled")
				self.parent.unbind('<Return>')
				self.b4.unbind 	  ('<Return>')

	def blur(self):
		self.f_im = gbl.input_im.crop((gbl.x1, gbl.y1, gbl.x2, gbl.y2))
		gbl.show_im = PIL.ImageTk.PhotoImage(self.f_im)
		self.canvas.itemconfig(gbl.f_im_c, image=gbl.show_im)
		self.canvas.coords(gbl.f_im_c, (gbl.x1+gbl.x2)/2, (gbl.y1+gbl.y2)/2)

	def re_start(self):
		gbl.go_restart = 1
		self.quit()
