from Tkinter import *
import tkMessageBox
from PIL import *
import os,sys
import PIL.Image
_imaging = PIL.Image.core
# from win32api import GetSystemMetrics
# own files
from my_globals import my_globals as gbl
import qual_window
import io_window
import crop_window
import restart_window
import error_window
import download_window
import upload_window
import reducer_window

def download_main():
	download = Tk()
	download.geometry("350x120+500+300")
	download.title("Download_Window")
	download_window.download_window(download)
	download.mainloop()
	download.destroy()

def upload_main():
	upload = Tk()
	upload.geometry("350x120+500+300")
	upload.title("Upload_Window")
	upload_window.upload_window(upload)
	upload.mainloop()
	upload.destroy()

def size_reducer_main():
	reducer = Tk()
	reducer.geometry("400x600+500+50")
	reducer.title("Image_Compression_Window")
	reducer_window.reducer_window(reducer)
	reducer.mainloop()
	reducer.destroy()

def error_main():
	error = Tk()
	error.geometry("290x150+500+300")
	error.title("404 NOT Found")
	error_window.error_window(error)
	error.mainloop()
	error.destroy()

def io_main():
	io = Tk()
	gbl.sc_w	 = io.winfo_screenwidth()
	gbl.sc_h	 = io.winfo_screenheight()
	io.geometry("350x120+500+300")
	io.title("IO_Window")
	io_window.io_window(io)
	io.mainloop()
	io.destroy()

def crop_main():
	crop = Tk()
	gbl.w,gbl.h = gbl.input_im.size
	gbl.mouse_x = gbl.w/2
	gbl.mouse_y = gbl.h/2
	width = gbl.w+200
	height = gbl.h
	crop.geometry(str(width)+'x'+str(height)+"+0+0")
	crop.title("Crop")
	crop_window.Crop_Window(crop)
	crop.mainloop()
	crop.destroy()

def quality_main():
	qual = Tk()
	width = gbl.x2-gbl.x1+200
	height = max(gbl.y2-gbl.y1, 200)
	qual.geometry(str(width)+'x'+str(height)+"+0+0")
	qual.title("Quality_Window")
	waste = qual_window.qual_window(qual)
	qual.mainloop()
	qual.destroy()

def restart_main():
	restart = Tk()
	restart.geometry("200x100+580+330")
	restart.title("Restart_Window")
	restart_window.restart_window(restart)
	restart.mainloop()
	restart.destroy()

# updating last address file
def update_file(w_file):
	w_file.truncate()
	w_file.write(str(gbl.cu_ind))
	w_file.write('\n')
	w_file.write(gbl.input_dir)
	w_file.write('\n')
	w_file.write(gbl.output_dir)
	w_file.write('\n')

# cropping and resizing and saving to windows
def start_process():
	gbl.input_im = PIL.Image.open(gbl.input_file)
	# resizing image to fit on screen
	im_w,im_h	 = gbl.input_im.size

	if((im_w+300) > gbl.sc_w or (im_h+100) > gbl.sc_h):
		gbl.r_factor=min((gbl.sc_w*1.0)/(im_w+300) , (gbl.sc_h*1.0)/(im_h+100))

	gbl.input_im.thumbnail((int(im_w*gbl.r_factor),int(im_h*gbl.r_factor)), PIL.Image.ANTIALIAS)

	temp_crop_im  = PIL.Image.open(gbl.input_file)
	temp_crop_im.thumbnail((int(im_w*gbl.r_factor),int(im_h*gbl.r_factor)), PIL.Image.ANTIALIAS)
	
	temp_main_crop_im = PIL.Image.open(gbl.input_file)
	# gbl.back == 0 implies to go on next Image
	gbl.back = 1
	while(gbl.back 	== 1):
		last_ind=gbl.cu_ind
		crop_main()
		if(gbl.exit == 1):
			sys.exit()
		if(gbl.skip == 1 or last_ind-gbl.cu_ind == 1 or gbl.go_restart == 1):
			gbl.skip = 0
			break
		gbl.back = 0
		size = gbl.width,gbl.height
		gbl.crop_im = temp_crop_im.crop((gbl.x1, gbl.y1, gbl.x2, gbl.y2))

		gbl.main_crop_im = temp_main_crop_im.crop((int(gbl.x1/gbl.r_factor), int(gbl.y1/gbl.r_factor), int(gbl.x2/gbl.r_factor), int(gbl.y2/gbl.r_factor)))
		gbl.main_crop_im.thumbnail((gbl.width,gbl.height), PIL.Image.ANTIALIAS)
		gbl.main_crop_im.save(gbl.output_file, gbl.out_format, quality=gbl.Quality, progressive=True, optimize=True)
		quality_main()

def reset_gbl():
	gbl.all_i_files=[]
	gbl.all_o_files=[]
	gbl.total_files=0
	gbl.last_start =0

def main():
	reset_gbl()
	io_main()
	if(gbl.exit 	  	== 1):
		sys.exit()
	if(gbl.last_start 	== 1):
		r_file 			= open("last_address.txt")
		gbl.cu_ind 		= int(r_file.readline())
		gbl.input_dir 	= r_file.readline().split('\n')[0]
		gbl.output_dir	= r_file.readline().split('\n')[0]
		r_file.close()
		if not (os.path.exists(gbl.input_dir) and os.path.exists(gbl.output_dir)):
			error_main()
			return
	if(gbl.download_prsd== 1):
		download_main()
		gbl.download_prsd= 0
	if(gbl.upload_prsd  == 1):
		upload_main()
		gbl.upload_prsd  = 0
	if(gbl.size_reducer == 1):
		size_reducer_main()
		gbl.size_reducer = 0
		return
	else:
		w_file			= open("last_address.txt", 'w')
		w_file.truncate()
		w_file.write(str(0))
		w_file.write('\n')
		try:
			temp = gbl.input_dir
			w_file.write(temp)
			w_file.write('\n')
			temp = gbl.output_dir
			w_file.write(temp)
			w_file.write('\n')
		except IOError:
			w_file.truncate()
			w_file.write(str(0))
			w_file.write('\n')
			temp = gbl.input_dir.split(' ')
			l = len(temp) 
			name=temp[0]
			for i in range(l):
				name+="\ "+temp[i]
			w_file.write(name)
			w_file.write('\n')
			temp = gbl.output_dir.split(' ')
			l = len(temp)
			name=temp[0]
			for i in range(l):
				name+="\ "+temp[i]
			w_file.write(name)
			w_file.write('\n')
		w_file.close()
	if(gbl.input_dir.endswith((".JPG", ".JPEG", ".PNG", ".psd", ".png", ".jpg", ".jpeg", ".jpg_2"))):
		gbl.input_file 	= gbl.input_dir
		temp = gbl.input_dir.split('/')
		l = len(temp)
		root = ""
		for i in range(l-1):
			root += "/"
			root += temp[i]
		name = temp[l-1]
		
		temp = gbl.output_dir.split('/')
		l = len(temp)
		outdir = ""
		for i in range(l-1):
			outdir += "/"
			outdir += temp[i]
		gbl.output_dir = outdir

		if not os.path.exists(outdir):
			os.makedirs(outdir)
		
		gbl.input_file  = str(root)+"/"+str(name)
		gbl.output_file = outdir   +"/"+str(name)
		start_process()
	
	else:
		for root, dirs, files in os.walk(gbl.input_dir):
			temp = str(root).split(gbl.input_dir)
			outdir = gbl.output_dir+temp[1]
			if not os.path.exists(outdir):
				os.makedirs(outdir)
			for name in files:
				if name.endswith((".JPG", ".JPEG", ".PNG", ".psd", ".png", ".jpg", ".jpeg", ".jpg_2")):
					gbl.input_file = str(root)+"/"+str(name)
					gbl.output_file = outdir+"/"+str(name)
					gbl.all_i_files.append(gbl.input_file)
					gbl.all_o_files.append(gbl.output_file)
					gbl.total_files+=1
				else:
					print name
		while (gbl.cu_ind<gbl.total_files):
			gbl.input_file 	= gbl.all_i_files[gbl.cu_ind]
			gbl.output_file = gbl.all_o_files[gbl.cu_ind]
			gbl.go_restart	= 0
			start_process()
			if(gbl.go_restart ==1):
				break
			w_file			= open("last_address.txt", 'w')
			update_file(w_file)
			w_file.close()
	if(gbl.go_restart==0):
		restart_main()

if __name__ == '__main__':
	while(gbl.exit!=1):
		main()
