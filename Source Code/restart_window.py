from Tkinter import *
from ttk import Style, Label
# own files
from main import *
from my_globals import my_globals as gbl

class restart_window(Frame):
  
	def __init__(self, parent):
		Frame.__init__(self, parent)   
		self.parent = parent
		self.initUI(parent)
		
	def initUI(self,parent):
		self.style = Style 	()
		self.style.theme_use("classic")
		Style().configure	("TLabel", font='serif 10', weight="Bold")

		# creating layout from frames
		self.frame1=Frame 	(parent)
		self.frame1.pack	(fill="both", expand="True")
		self.frame2=Frame 	(parent)
		self.frame2.pack	(fill="both", expand="True")

		# putting text in frame1
		Label				(self.frame1, text="Completed!! \n Do you want to EXIT?", font = "Helvetica 10 bold").pack(side="bottom", anchor='center')

		# putting button in frame2
		self.b10 = Button	(self.frame2 , text="Yes"	, width=7, state="active", font='serif 10', command=self.yes_clicked)
		self.b11 = Button	(self.frame2 , text="No"	, width=7, state="active", font='serif 10', command=self.no_clicked)
		self.b10.pack		(side="left" , padx=8)
		self.b11.pack		(side="left" , padx=8)
		self.b10.bind		('<Return>'	 , self.yes_clicked)
		self.b11.bind		('<Return>'	 , self.no_clicked )

	def yes_clicked(self,*args):
		gbl.exit=1
		self.quit()

	def no_clicked(self,*args):
		gbl.exit=0
		self.quit()	