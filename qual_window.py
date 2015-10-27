from Tkinter import *
from ttk import Style, Label, Scale
from PIL import *
import os,sys
import PIL.Image
import PIL.ImageTk
# own files
from main import *
from my_globals import my_globals as gbl

# print '\n','\n',"Yes",'\n','\n'

class qual_window(Frame):
  
	def __init__(self, parent):
		Frame.__init__(self, parent)   
		self.parent = parent
		self.initUI(parent)
		
	def initUI(self,parent):
		# initalising some variables
		self.Quality_e = None
		self.scale 	   = None
		self.fmemory_e = None
		self.memory_e  = None

		self.style = Style()
		self.style.theme_use("classic")
		Style().configure	("TEntry", font='serif 10')
		Style().configure	("TLabel", font='serif 10')

		# creating menubar
		menubar = Menu(self.parent)
		self.parent.config(menu=menubar)
		
		fileMenu = Menu(menubar)
		fileMenu.add_command(label="Restart", command=self.re_start)
		menubar .add_cascade(label="Options", menu=fileMenu)

		# creating layout from frames
		self.frame3=Frame 	(parent, relief="sunken")
		self.frame3.pack	(side="bottom", fill=X)
		self.frame1=Frame 	(parent, relief="sunken")
		self.frame1.pack	(side="left", fill=Y)
		self.frame2=Frame 	(parent, width=gbl.x2-gbl.x1, height=max(gbl.y2-gbl.y1, 200), relief="flat", bg="#333")
		self.frame2.pack	(side="right", fill="both", expand="True")

		# creating canvas in frame 2
		self.canvas = Canvas(self.frame2)
		self.canvas.pack	(fill="both", expand="True")

		# creating save and next Button
		self.b9 = Button	(self.frame1, text="Save and Next>>", state="active", font='serif 10', command=self.save_next)
		self.b9.pack		(side="bottom", pady=5)
		self.b9.bind		('<Return>', self.save_next)
		self.b8 = Button	(self.frame1, text="<<Back", state="active", font='serif 10', command=self.go_back)
		self.b8.pack		(side="bottom", pady=5)
		self.b8.bind		('<Return>', self.go_back)
		self.parent.bind	('<Return>', self.save_next)

		# track for editable entries
		self.e1s = StringVar(self.frame1)
		self.e2s = StringVar(self.frame1)
		self.e1s.trace		("w", self.check)
		self.e2s.trace		("w", self.check)

		# creating editable format and quality entries
		# self.format_e = self.make_entry(gbl.out_format, "Format (Default JPEG)")
		self.format_e = Entry(self.frame1, textvariable = self.e1s, bg="white", bd=4, cursor="xterm", fg="Black", justify="center", relief="ridge")
		self.format_e.insert (0,"JPEG")
		self.format_e.pack	 (side="top")
		Label				 (self.frame1, text="Format (Default JPEG)").pack(side="top")

		# self.Quality_e = self.make_entry(gbl.Quality, "Format (Default 80)")
		self.Quality_e = Entry(self.frame1, textvariable = self.e2s, bg="white", bd=4, cursor="xterm", fg="Black", justify="center", relief="ridge")
		self.Quality_e.insert (0,gbl.Quality)
		self.Quality_e.pack	  (side="top")
		Label				  (self.frame1, text="Quality (Default 80)").pack(side="top")
		# self.format_e.config(textvariable=self.e1s)
		# self.Quality_e.config(textvariable=self.e2s)

		# creating sliding bar
		self.var = IntVar	()
		self.scale = Scale 	(self.frame1, from_=1, to=100, orient="horizontal", length=168, command=self.onScale)
		self.scale.set 		(gbl.Quality)
		self.scale.pack		(side="top")

		self.l1 = Label		(self.frame1, textvariable=self.var)
		self.l1.pack		(side="top")
		self.var.set 		(gbl.Quality)

		# saving and putting PIL.Image in canvas
		self.save_put_image()

		# creating memory entries
		self.fmemory_e = self.set_memory_entry(self.frame1, "Final", gbl.output_file)
		self.memory_e = self.set_memory_entry(self.frame1, "Initial", gbl.input_file)

		# creating status bar
		Label					(self.frame3, text=gbl.output_file) 						.pack(side="left" , anchor="w")
		Label					(self.frame3, text=str(gbl.cu_ind)+"/"+str(gbl.total_files)).pack(side="right", anchor="e")	

	# def make_entry(self, data, text_):
	# 	temp_entry = Entry(self.frame1, textvariable=None, bg="white", bd=4, cursor="xterm", fg="Black", justify="center", relief="ridge")
	# 	temp_entry.insert(0,data)
	# 	temp_entry.pack(side="top")
	# 	Label(self.frame1, text=text_).pack(side="top")
	# 	return temp_entry

	def quality_entered(self):
		gbl.out_format 	= 	str(self.format_e. get())
		gbl.Quality 	= 	int(self.Quality_e.get())
		if(self.scale  != None):
			self.scale.set 	   (gbl.Quality)
			self.var.set 	   (gbl.Quality)
			self.save_put_image()

	def onScale(self, val):
		v = 			  	int(float(val))
		self.var.set 		   (v)
		self.Quality_e.delete  (0,'end')
		self.Quality_e.insert  (0,v)

	def check(self, *args):
		if(self.Quality_e != None):
			e1_data=self.e1s.get()
			e2_data=self.e2s.get()
			if (e1_data in ["JPEG", "PNG"]) and e2_data.isdigit() and int(e2_data)<=100 and int(e2_data)>0:
				self.b9.config(state="active")
				self.b9.bind('<Return>', self.save_next)
				self.quality_entered()
			else:
				self.b9.config(state="disabled")
				self.b9.unbind('<Return>')

	def save_next(self, *args):
		if(os.path.isfile(gbl.output_file+"temp")):
			os.remove(gbl.output_file+"temp")
		self.quit()

	def go_back(self, *args):
		if(os.path.isfile(gbl.output_file+"temp")):
			os.remove(gbl.output_file+"temp")
		gbl.back = 1
		gbl.cu_ind-=1
		self.quit()

	def save_put_image(self):
		if(os.path.isfile(gbl.output_file)):
			os.remove(gbl.output_file)
		if(os.path.isfile(gbl.output_file+"temp")):
			os.remove(gbl.output_file+"temp")
		gbl.crop_im.save(gbl.output_file+"temp", gbl.out_format, quality=gbl.Quality, progressive=True, optimize=True)
		gbl.main_crop_im.save(gbl.output_file  , gbl.out_format, quality=gbl.Quality, progressive=True, optimize=True)
		self.temp_im 		= PIL.Image.open(gbl.output_file+"temp")
		self.fc_im 	 		= PIL.ImageTk.PhotoImage(self.temp_im)
		gbl.crop_im_canv 	= self.canvas.create_image((gbl.x2-gbl.x1)/2,max(gbl.y2-gbl.y1,600)/2, image=self.fc_im)
		if(self.fmemory_e  != None):
			self.memory 	= (os.path.getsize(gbl.output_file)*1.0)/1024
			self.fmemory_e.config(state="normal")
			self.fmemory_e.delete(0,'end')
			self.fmemory_e.insert(0,self.memory)
			self.fmemory_e.config(state="readonly")

	def set_memory_entry(self, framei, text_, file_name):
		temp_entry = Entry(framei, bg="white", bd=4, cursor="xterm", fg="Black", justify="center", relief="ridge")
		memory = (os.path.getsize(file_name)*1.0)/1024
		temp_entry.insert(0,memory)
		temp_entry.config(state="readonly")
		temp_entry.pack(side="top")
		Label(framei, text=text_+" Memory (KB)").pack(side="top")
		return temp_entry

	def crop_size(self):
		if((gbl.w*1.0)/gbl.h>=(int(gbl.width)*1.0)/int(gbl.height)):
			cropx = ((gbl.height*gbl.w)-	(gbl.width*gbl.h))/(gbl.height*2)
			cropy = 0
		else:
			cropx = 0
			cropy = ((gbl.width*gbl.h) -	(gbl.height*gbl.w))/(gbl.width*2)
		return cropx,cropy

	def re_start(self):
		gbl.go_restart = 1
		self.quit()