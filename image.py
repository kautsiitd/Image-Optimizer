import os,sys
import Image
import glob
import ImageFilter

width = 1080
height = 1920
size = width,height
base_quality = 0			# set base_quality of image
center_x = width/2
center_y = height/2
out_format = "JPEG"			# either "JPEG" or "PNG"
lower_m_limit = 50*1024		# in bytes
upper_m_limit = 1550*1024
lower_quality = 0
upper_quality = 0			# should not greater than 100
count =0

for root, dirs, files in os.walk("/home/kauts/Desktop/Qutub"):
	temp = str(root).split("/Qutub")
	outdir = temp[0]+"/Output_images"+temp[1]
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	for name in files:
		if name.endswith((".JPG", ".JPEG", ".PNG", ".psd", ".png", ".jpg", ".jpeg", ".jpg_2")):
			outfile=outdir+"/"+str(name)+".thumbnail"
			if name != outfile:
				try:
					location = str(root)+"/"+str(name)
					im = Image.open(location)
					w,h=im.size
					if((w*1.0)/h>=(width*1.0)/height):
						cropx=((16*w)-(9*h))/32
						cropy=0
						im=im.crop((cropx,cropy,w-cropx,h-cropy))
					else:
						cropx=0
						cropy=((9*h)-(16*w))/18
						im=im.crop((cropx,cropy,w-cropx,h-cropy))
					m_size = 0	# size of output file
					temp_quality=base_quality
					while m_size<lower_m_limit and temp_quality<=upper_quality:
						print "l",m_size,temp_quality
						if os.path.exists(outfile):
							os.remove(outfile)
						im.thumbnail(size, Image.ANTIALIAS)
						im.save(outfile, out_format, quality=temp_quality, progressive=True, optimize=True, dpi=(1000,100))
						m_size = os.path.getsize(outfile)
						temp_quality+=5
					while m_size>upper_m_limit and temp_quality>=lower_quality:
						print "u",m_size,temp_quality
						if os.path.exists(outfile):
							os.remove(outfile)
						im.thumbnail(size, Image.ANTIALIAS)
						im.save(outfile, out_format, quality=temp_quality, progressive=True, optimize=True, dpi=(1000,1000))
						m_size = os.path.getsize(outfile)
						temp_quality-=5
				except IOError:
					count=count+1
					print count
					# print "cannot create thumbnail for '%s'" % location
		else:
			print name