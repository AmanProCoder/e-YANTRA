'''
What is an image?
A camera that records images passing through the camera's lens on film is called a film camera 

Components of the Modern digital Cameras- 
Lens- Focuses all the info 
photo sensitive sensor
image processing engine-process the content stored by the sensor
memory storage 

Image is represented as matrix
On a grayscale spectrum the color grade can vary from 0 to infinity 
But to use it here in the computer we need to do the QUANTISATION(Converting it into 0 to 255)
Converted into 256 pieces and every piece represents one shade of the grey 
0 is fully black 
255 is fully white 

greyscale image is a 2D(M x N) matrix and 
RGB image is a 3D(M x N x 3) matrix(heigh, width, channel )

What is Pixel?
Pixel represents the smallest unit of an image 
each pixel has a value between 0-255 based on the color(represented by 8 bits in binary )

What is the size of the grayscale with dimension  32x32?
32x32x1 bytes = 1kb

In RGB, one pixel occupies 3 Bytes 


Computer vision refers to high level understanding of images - detecting face, object, tracking, etc


Image processing(it is a subpart of the CV) such as detecting shapes, removing noises, detecting edges or corners, etc 

'''
