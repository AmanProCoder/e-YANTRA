
from configparser import Interpolation
from tkinter import image_names
import cv2
import numpy as np
# # loading and displaying and saving image
# cv2.imread()
# cv2.imshow()
# cv2.imwrite()

# # Image resizing and rotation 
# cv2.resize()
# getRotationMatrix2d()

# #Drawing Function in OpenCV
# cv2.line()       #draw line 
# cv2.rectangle()  #draw rectangle 
# cv2.circle()     #draw circle 
# cv2.putText()    #Write text 



image = cv2.imread("picture.png")
# print(type(image))   #prints numpy array 
# print(image)

# cv2.imshow("image",image)  #first arg is window image 
# cv2.waitKey(0)  #0 is used so that it holds the image for infinite time untill a key is pressed
# #it takes arg in milliseconds and if we will put arg as 2000 then it will hold for 2 sec
# cv2.destroyAllWindows()

# dimension=image.shape   # height x width x channel(format)
# print("\nImage dimension is:",dimension)



image_gray=cv2.imread("picture.png",0)
# cv2.imshow("grayimage",image_gray)
# cv2.waitKey(0)
# dimension=image_gray.shape   # height x width (format)
# print("\nImage dimension is:",dimension)

#saving the image
# cv2.imwrite("opencvLogoOpenCV.png",image_gray)



# pixel_gray=image_gray[120,120]
# print("Pixel color:",pixel_gray)
# pixel_rgb=image[120,120,:]  #
# print("pixel color:",pixel_rgb) # blue green red (format)

# Accessing a pixel and changing its value 
# image[120,120,:]=[255,255,255]
# cv2.imshow("changed",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Accessing region of interest(ROI)

# image[0:250,0:250,:]=[0,0,0]   #access a square of area 250 x 250
# cv2.imshow("new image",image)
# cv2.waitKey(0)  
# cv2.destroyAllWindows()

# Cropping an image using array slicing 
# image_cropped=image[0:205,0:205,:]
# cv2.imshow("cropped image",image_cropped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Checking out individual channel of an RGB Image
# image_b_channel=image[:,:,0]
# image_g_channel=image[:,:,1]
# image_r_channel=image[:,:,2]

# cv2.imshow("image_b_channel",image_b_channel)
# cv2.waitKey(0)
# cv2.imshow("image_g_channel",image_g_channel)
# cv2.waitKey(0)
# cv2.imshow("image_r_channel",image_r_channel)
# cv2.waitKey(0)

# Resize an image height and width without preserving aspect ratio-cv2.resize()

# height,width, _ = image.shape
# width=500
# height=100
# image=cv2.resize(image,(width,height),interpolation=cv2.INTER_LINEAR) 
# #for refernce of interpolatin techinques: https://docs.opencv.org/3.4/da/d54/group__imgproc__transform.html
# cv2.imshow("resized image",image)
# cv2.waitKey(0)

# Resize an image height and width preserving aspect ratio-cv2.resize()

# image=cv2.imread("picture.png")
# scale_factor=0.2
# height,width, _ = image.shape
# width=int(width*scale_factor)  #image dimension needs to be in the int only, it cant be in float value
# height=int(height*scale_factor)
# image=cv2.resize(image,(width,height),interpolation=cv2.INTER_LINEAR) 
# cv2.imshow("resized image with preserving aspect ratio",image)
# cv2.waitKey(0)


# Rotating an image 

image=cv2.imread("picture.png")
scale_factor=1.0
height,width, _ = image.shape
angle_of_rotation=45
centre_of_rotation=(int(width/2),int(height/2))

M=cv2.getRotationMatrix2D(centre_of_rotation,angle_of_rotation,scale_factor)

rotated=cv2.warpAffine(image,M,(width,height))
cv2.imshow("rotated",rotated)
cv2.waitKey(0)



# find how to access a single channel of the image