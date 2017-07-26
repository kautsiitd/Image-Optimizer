# Introduction

This project contains a GUI created using python Tkinter which helps in **Cropping, Resizing, Reducing Size from individual image to Images in bulk Offline.** With the help of this repo you can also **Download or Upload Images to your S3 bucket in bulk in minimal time with just few clicks.** This repo also provides feature with the help of which **you can start your work from where you left last time**.

Brief description on individual window levels can be found in file [Description.pdf](Description.pdf).

# Installation

1. First you will have to download this repo, for this you can either directly download zip file from above or you can also run *git clone https://github.com/kautsiitd/Image-Extractor-for-Excel.git* in terminal to clone this repo.
2. Then you will have to make sure that you have following things for sure to make this work:
  * python (>=2.7.10)
  * pip
  * PIL
  * Tkinter
  * numpy
  * boto

  You can follow instruction in [Help.txt](Help.txt) to find out commands to install these on different platforms.

3. After that you just need to cd to *Source Code* folder and run **python main.py**

That's it, after this IO window will pop up and you will also have different options at top for different functionality. You can follow **How It Works** section below to see how different sections can be accessed and corresponding flow charts.

# How It Works
Follow these steps and flow chart to see how this application works and what all features it has.

## Manual Image Optimizer

![alt tag](Readme%20Images/Single_Image_FlowChart.png)

After following installation section instructions, you should be able to run *python main.py*. After this a window will pop up named **IO_Window** where you can follow above flow chart or say following steps demonstrated in above flow chart:
1. Select **Input Directory** by just clicking that button and choosing target folder.

**You can also choose one single file as input file** instead of whole directory from option **Open** at top and then select **Input File** option.

2. Similarly you have to choose **Output Directory** where you want to save all files.

**Note:** You can also choose **From Last** button if you want to continue from where you left last time.

3. Click **Next** and **Crop Window** will open.
  * Here you can choose the size of image in Pixels for height and width separately which will show the cropped picture as highlighted Image(to maintain the ratio of height and width which is entered).
  * You can **Keep the aspect ratio** if you do not want to crop Image but want to reduce pixels for height and width. Obviously In this case, you can only edit height or width of picture because ratio needs to be maintained.
  * You can also choose **Skip** option at bottom to skip the Image in which you do not want any change. But in that case Original pic would be saved in destination folder.
  * You can see Image Path and number of Images that is remaining to optimize in bottom left and right Section.
  * Using **Exit** you can exit from GUI any time, and **Don't worry because you can always start from where you left using From Last button in IO_Window at beginning.**
  * You can Click **Next** to go to next step, **Quality_Window**.
  * You can also go back to previous pic and update it using **Back** button.

4. Click **Next** and **Quality Window** will open.
  * Here you can choose format of Image in which you want to save Image. For now it can be only **JPEG** and **PNG**.
  * You can select Quality of Image either using slider or manually entering it in text box. **Quality of Image will only be effective if format in which you are saving image is JPEG**.
  * You can see live changes in photo when you will change format of Image or Quality of Image side by side.
  * You can see final Image size and Initial Image size so that **you can make an informed decision about what memory and Quality combination is Perfect for you.**
  * You can go back to Crop Window using **Back** button if you want to change dimension of image again.
  * You can click on **Save and Next** button and it will just save optimized Image at destination folder by **keeping hierarchy of Input folder in Output folder using same name as it is in Input Folder**. And after this you will lead to next Image if there would be any.

That's it, using following steps you can optimize single image or images in bulk by making informed decision about memory and Quality combination. Using From Last option you can always start from where you left last time.

## Automatic Image Optimizer

![alt tag](Readme%20Images/BulkResizing_Image_FlowChart.png)

Using this software you can also optimize, resize and crop Images in bulk. You just have to choose some parameters and in one click all images will be optimized and saved to destination folder. Here I am adding few steps, features and Importance of each variable to proceed:

1. After Initiating software using python main.py, IO_Window opens up first.
2. In top bar you can click **Other** and then select **Size Reducer** to open **Image Compression Window**.
3. Here are few fields for various variables that you have to fill to optimize Images accordingly:
  * **Input Directory:** Folder where all Images are stored.

  **Note:** It will consider Images having extension among these -> JPG, JPEG, PNG, psd, tif, tiff.

  * **Output Directory:** Folder where you want to save all optimized images in same hierarchy and name as it is in Input Directory.
  * **Min/Max Memory:** Memory under which you want to be all you Images.

  **Note:** Memory parameter will be compromised if Image with lowest Quality having memory space above than Max Memory limit.

  * **Min/Max Quality:** Range in which quality of Image will vary if optimized image at certain quality does not lie under memory limit. If memory of optimized image lie in memory range then it will try to increase quality till Max limit until memory space goes out of bound.

  * **Base Quality:** It will be the starting point of quality of Image from where It will move towards min or max limit to make sure that optimized Image will lie in memory range with best quality possible.

  **Note:** Quality variables would not be effective if format of optimized Image is set to be **other than JPEG.**

  * **Format:** Right now this software is only supporting **JPEG and PNG** for optimized images. Obviously image size for JPEG will be less.

  * **Resolution:** If you want to resize all Images, you can set width and height separately in terms of *pixels*. If you do not want to crop Images but still want to resize it to certain pixels in one direction then you can also fill **A/c h** or **A/c w** in one of the fields accordingly.

  **Note:** Image will be center cropped.

  * **Optimize, Center Crop, Encode:** These variables are not working right now as it is not coded yet. So I will suggest to tick all of the options always.

  * **Default:** This will just fill up some best basic parameters in all fields. But it is not necessary that it will result in best optimized Images, You can choose above variables according to your need.

4. Click **Compress**, and all optimized images will be saved in destination folder with same hierarchy and names as it was in Input Directory.

Thats it, You can follow progress of image optimization process in terminal, saying:
* Current image it is compressing.
* How many it has already compressed.
* Total number of Images in folder that it is going to compress.
* Size and quality of images that it already has compressed.

After process is done, Restart Window will open saying that operations have completed on all Images in Input Folder.

## Downloading and Uploading Files/Folders to S3

You can also download and upload whole folders using this software in just few clicks.

**NOTE: You will have to set AWS_KEY and AWS_SECRET in** [s3_window.py](Source%20Code/s3_window.py) **file to make this work.**

![alt tag](Readme%20Images/Download_Upload_S3.png)

You can follow above flow chart to see what and how you can do things here. You can also follow steps below for same:

1. After Initiating software using python main.py, IO_Window opens up first.
2. In top bar you can click **S3_Bucket** and then select **Upload/Download** to open **Upload_Window/Download_Window**.
3. Now you have to select **From** and **To** directory by clicking just clicking on corresponding buttons.
  * If you are **Downloading** from S3, then From text field will contain path of folder on S3 which you wish to download, and TO text field will contain path of folder where you want to download your files on your local machine. You can either manually enter these paths or can select folder by clicking on *From* and *To* buttons
  * If you are **Uploading** to S3, then From text field will contain path of folder on local machine which you want to upload on S3 and To text field will contain path of folder on S3 where you want to upload this folder. You can either manually enter these paths or can select folder by clicking on *From* and *To* buttons

  **NOTE: I will suggest to enter S3 related Paths manually because It will may take too much to fetch all names in folder to show you what is there in a folder on S3.** ***This will happen because paging is not yet implemented in software.***

  **NOTE:** Format for folder path in S3 would be like this, *S3://folder1/folder2....*, where S3:// is just representing home address.

Thats it, After selecting both input and output directory, You just have to click Download/Upload button to perform execution and **It will Upload/Download files in same hierarchy as it is in original folder**. You can follow progress of Downloading/Uploading in terminal, saying:

* Current file name and number it is Uploading/Downloading.
* Total Number of files it has to Upload/Download.

# Need Help/Issues

If you find some issue or require some help then you can report about it in [Issues](https://github.com/kautsiitd/Image-Optimizer/issues).
