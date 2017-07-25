import os,sys
try:
    import Image
except:
    from PIL import Image
try:
    import ImageFilter
except:
    from PIL import ImageFilter # ownfiles
from my_globals import my_globals as gbl
class size_reduce:
    def __init__(self):
        self.i_dir = str(gbl.input_dir)
        self.o_dir = str(gbl.output_dir)
        self.width = gbl.width
        self.height = gbl.height
        self.base_quality = gbl.bse_q
        # set self.base_quality of image
        # self.center_x = self.width/2
        # self.center_y = self.height/2
        self.out_format = gbl.form # either "JPEG" or "PNG"
        self.lower_m_limit = gbl.min_m*1024 # in bytes
        self.upper_m_limit = gbl.max_m*1024
        self.lower_quality = gbl.min_q
        self.upper_quality = gbl.max_q
        # should not greater than 100 self.count =0
        self.not_done=0
        self.reduce_it()

    def reduce_it(self):
        for root, dirs, files in os.walk(self.i_dir):
            for name in files:
                if name.endswith((".JPG", ".JPEG", ".PNG", ".psd", ".png", ".jpg", ".jpeg", ".jpg_2", ".tif", "TIF",
                ".tiff", ".TIFF", "_png", "_PNG")):
                    only_name=str(name).split('.')
                    # print only_name,str(name)
                    outfile=""
                    if(str(root).split(self.i_dir)[1]==""):
                        outfile=self.o_dir+"/"+str(name)
                    else:
                        outfile=self.o_dir+"/"+str(root).split(self.i_dir)[1]+"/"+str(name)

                    try:
                        o_location = str(root)+"/"+str(name)
                        im = Image.open(o_location)
                        size = self.set_size(im.size)
                        im.thumbnail(size, Image.ANTIALIAS)
                        m_size = os.path.getsize(o_location)
                        temp_quality=self.base_quality
                        if(m_size<self.upper_m_limit):
                            temp_quality = 90
                            im.save(outfile,
                                    self.out_format,
                                    quality=temp_quality,
                                    progressive=True,
                                    optimize=True)
                            save_size=os.path.getsize(outfile)

                        while save_size>m_size and temp_quality>self.lower_quality:
                            temp_quality-=5
                            if os.path.exists(outfile):
                                os.remove(outfile)
                            im.save(outfile,
                            self.out_format,
                            quality=temp_quality,
                            progressive=True,
                            optimize=True)
                            save_size=os.path.getsize(outfile)
                            # print temp_quality
                            self.count+=1
                            continue

                        while m_size>self.upper_m_limit and temp_quality>=self.lower_quality:
                            # print "u",m_size,temp_quality if os.path.exists(outfile):
                            os.remove(outfile)
                            im.save(outfile,
                                    self.out_format,
                                    quality=temp_quality,
                                    progressive=True,
                                    optimize=True)
                            m_size = os.path.getsize(outfile)
                            temp_quality-=5

                        while m_size<self.lower_m_limit and temp_quality<=self.upper_quality:
                            # print "l",m_size,temp_quality
                            if os.path.exists(outfile):
                                os.remove(outfile)
                            im.save(outfile,
                                    self.out_format,
                                    quality=temp_quality,
                                    progressive=True,
                                    optimize=True)
                            m_size = os.path.getsize(outfile)
                            temp_quality+=5

                        self.count=self.count+1
                        sys.stdout.flush()
                        print "\r",
                        print "done",self.count,"files",
                    except IOError:
                        self.not_done+=1
                        print self.not_done
                        print "cannot create thumbnail for '%s'" % o_location
                else:
                    self.not_done+=1
                    print name

    def set_size(self,(w,h)):
        if(self.width == "A/c h"):
            self.width = (h*int(self.height)*1.0)/w
        elif(self.height == "A/c w"):
            self.height = (w*int(self.width)*1.0)/h
            return int(self.width),int(self.height)
