import numpy as np
import cv2

'''

Techniques used to remove the noises from the background
Erosion decreases 
Dilation expands the boundary of white areas

Contour Detection:(if any object is been detected then its boundary is called as contour)
Contour can be explained simply as a curve joining all the continuous points(along the boundary), having sme color or intensity 
Contour are always closed curves, never open.
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

        # Step 2: select lower and upper bounds for color filtering to create a mask 
        lower=np.array([0,85,176])
        upper=np.array([40,255,255])
        mask=cv2.inRange(hsv_image,lower,upper)

        # Step 3: Remove noise in image
        kernel=np.ones((5,5),np.uint8)
        mask=cv2.erode(mask,kernel,iterations=1)

        # Step 4: Find and draw contours
        contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        frame=cv2.drawContours(frame,contours,-1,(0,0,255),3)
        print(contours)

        # Step 5: Take only largest contours as the main contours
        main_contour=[]
        for cnt in contours:
            area=cv2.contourArea(cnt)
            if(area>200):
                main_contour.append(cnt)
        frame=cv2.drawContours(frame,main_contour,-1,(0,0,255),3)

        # Step 6: Calculate the centroid of the object
        try:
            M=cv2.moments(main_contour[0])
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            print(M)

            text=str((cx,cy))
            frame=cv2.putText(frame,text,(cx,cy),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255),2)
        except Exception as e:
            print(e)
            pass

        # Displaying the resulting frame
        cv2.imshow("frame",frame)
        # cv2.imshow("HSV",hsv_image)
        cv2.imshow("mask",mask)

        if cv2.waitKey(1) & 0xFF==ord('q'):    #we cant write 0 here, because we want to keep on updating the frames
            break                              # "q" button is set as the quitiing button

