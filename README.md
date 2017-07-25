# Introduction

This project contains a GUI created using python Tkinter which helps in **Cropping, Resizing, Reducing Size from individual image to Images in bulk Offline.** With the help of this repo you can also **Download or Upload Images to your S3 bucket in bulk in minimal time with just few clicks.** This repo also provides feature with the help of which **you can start your work from where you left last time**.

Brief description on individual window levels can be found in file **Description.pdf**.

# Installation

1. First you will have to download this repo, for this you can either directly download zip file from above or you can also run *git clone https://github.com/kautsiitd/Image-Extractor-for-Excel.git* in terminal to clone this repo.
2. Then you will have to make sure that you have following things for sure to make this work:
  * python (>=2.7.10)
  * pip
  * PIL
  * Tkinter
  * numpy
  * boto

  You can follow instruction in Help.txt to find out commands to install these on different platforms.
3. After that you just need to cd to *Source Code* folder and run **python main.py**

That's it, after this IO window will pop up and you will also have different options at top for different functionality. You can follow **How It Works** section below to see how different sections can be accessed and corresponding flow charts.

# How It Works
Follow these steps and flow chart to see how this application works and what all features it has.
  ## Manual Image Optimizer

    ![alt tag](https://github.com/kautsiitd/Image-Optimizer/blob/master/Single_Image_FlowChart.png)

    After following installation section instructions, you should be able to run *python main.py*. After this a window will pop up named **IO_Window** where you can follow above flow chart or say following steps demonstrated in above flow chart:
    1. Select **Input Directory** by just clicking that button and choosing target folder.

    **You can also choose one single file as input file** instead of whole directory from option **Open** at top and then select **Input File** option.
    2. Similarly you have to choose **Output Directory** where you want to save all files.
    **Note:** You can also choose **From Last** button if you want to continue from where you started.
    3. Click **Next** and **Crop Window** will open.
      * Here you can choose the size of image in Pixels for height and width separately which will show the cropped picture as highlighted Image(to maintain the ratio of height and width which is entered).
      * You can **Keep the aspect ratio** if you do not want to crop Image but want to reduce pixels for height and width. Obviously In this case, you can only edit height or width of picture because ratio needs to be maintained.
      * You can also choose **Skip** option at bottom to skip the Image in which you do not want any change. But in that case Original pic would be saved in destination folder.
      * You can see Image Path and number of Images that is remaining to optimize in bottom left and right Section.
      * Using **Exit** you can exit from GUI any time, and **Don't worry because you can always start from where you left using From Last button in IO_Window at beginning.**
      * You can Click **Next** to go to next step, **Quality_Window**.
      * You can also go back to previous pic and update it using **Back** button.
    4. Click **Next** and **Quality_Window** will open.
      * Here you can choose format of Image in which you want to save Image. For now it can be only **JPEG** and **PNG**.
      * You can select Quality of Image either using slider or manually entering it in text box. **Quality of Image will only be effective if format in which you are saving image is JPEG**.
      * You can see live changes in photo when you will change format of Image or Quality of Image side by side.
      * You can see final Image size and Initial Image size so that **you can make an informed decision about what memory and Quality combination is Perfect for you.**
      * You can go back to Crop Window using **Back** button if you want to change dimension of image again.
      * You can click on **Save and Next** button and it will just save optimized Image at destination folder by **keeping hierarchy of Input folder in Output folder using same name as it is in Input Folder**. And after this you will lead to next Image if there would be any.

    That's it, using following steps you can optimize single image or images in bulk by making informed decision about memory and Quality combination. Using From Last option you can always start from where you left last time.


# Customization


# Motivation


# Need Help/Issues
