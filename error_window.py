from Tkinter import *
from ttk import Style, Label
# own files
from main import *
from my_globals import my_globals as gbl

class error_window(Frame):
  
	def __init__(self, parent):
		Frame.__init__(self, parent)   
		self.parent = parent
		self.initUI(parent)
		
	def initUI(self,parent):
		self.style = Style 	()
		self.style.theme_use("classic")
		Style().configure	("TLabel", font='serif 10', weight="Bold")

		# creating layout from frames
		self.frame0=Frame 	(parent)
		self.frame0.pack	(fill="both", expand="True")
		self.frame1=Frame 	(parent)
		self.frame1.pack	(fill="both", expand="True")
		self.frame2=Frame 	(parent)
		self.frame2.pack	(fill="both", expand="True")
		self.frame3=Frame 	(parent)
		self.frame3.pack	(fill="both", expand="True")
		self.frame4=Frame 	(parent)
		self.frame4.pack	(fill="both", expand="True")
		self.frame5=Frame 	(parent)
		self.frame5.pack	(fill="both", expand="True")

		# putting text in frame1
		msg1 	   =		"File or Directory not found:"
		msg2	   =		"1. It has been deleted"
		msg3	   =		"2. Was never created"
		msg4	   =		"3. Someone has modified file 'last_address.txt'"
		msg5	   =		"Please re-enter address"
		Label				(self.frame0, text=msg1, font = "Helvetica 11 bold", anchor='center').pack(side="top")
		Label				(self.frame1, text=msg2, font = "Helvetica 10	  ", anchor='nw'	).pack(side="left", padx=5)
		Label				(self.frame2, text=msg3, font = "Helvetica 10	  ", anchor='nw'	).pack(side="left", padx=5)
		Label				(self.frame3, text=msg4, font = "Helvetica 10	  ", anchor='nw'	).pack(side="left", padx=5)
		Label				(self.frame4, text=msg5, font = "Helvetica 11 bold", anchor='center').pack(side="top")

		# putting button in frame2
		self.b12 = Button	(self.frame5 , text="Ok"	, width=7, state="active", font='serif 10', command=self.clicked)
		self.b12.pack		()
		self.b12.bind		('<Return>'	 , self.clicked)

	def clicked(self, *args):
		self.quit()