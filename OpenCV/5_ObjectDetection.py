import numpy as np
import cv2

'''

Techniques used to remove the noises from the background
Erosion decreases 
Dilation expands the boundary of white areas

'''

if __name__=="__main__":
    vid=cv2.VideoCapture(0) #0 is for the inbuild camera
    # Normal capturing my the vidcam 
    # while(True):
    #     ret,frame=vid.read()
    #     cv2.imshow("frame",frame)
    #     if cv2.waitKey(1) & 0xFF==ord('q'):
    #         break

    while(True):
        ret,frame=vid.read()
        # Step 1: Convert frame to HSV
        hsv_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower=np.array([0,85,176])
        upper=np.array([40,255,255])
        mask=cv2.inRange(hsv_image,lower,upper)


        # Displaying the resulting frame
        cv2.imshow("frame",frame)
        # cv2.imshow("HSV",hsv_image)
        cv2.imshow("mask",mask)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
