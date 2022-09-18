import numpy as np
import cv2

canvas=np.zeros((500,500,3),np.uint8)
# cv2.imshow("canvas",canvas)
# cv2.waitKey(0)


# draw line - cv2.line()
pt1=(499,0)
pt2=(0,499)
color=(0,0,255)
thickness=3

canvas=cv2.line(canvas,pt1,pt2,color,thickness)
# cv2.imshow("canvas",canvas)
# cv2.waitKey(0)


# Draw rectangle cv2.rectangle()
pt1=(200,200)
pt2=(300,300)
thickness=3

canvas=cv2.rectangle(canvas,pt1,pt2,color,thickness)
# cv2.imshow("canvas",canvas)
# cv2.waitKey(0)


# Draw circle - cv2.circle()
pt=(250,250)
radius=70
color=(255,0,0)

canvas=cv2.circle(canvas,pt,radius,color,thickness)
# cv2.imshow("canvas",canvas)
# cv2.waitKey(0)


#Creating something fun

canvas=np.zeros((500,500,3),np.uint8)

canvas=cv2.circle(canvas,(250,250),30,(0,255,0),3)

canvas=cv2.line(canvas,(100,200),(250,100),(0,255,0),thickness)
canvas=cv2.line(canvas,(250,100),(302,200),(0,255,0),thickness)
canvas=cv2.line(canvas,(302,200),(100,200),(0,255,0),thickness)

canvas=cv2.line(canvas,(250,100),(250,200),(0,255,0),thickness)


font=cv2.FONT_HERSHEY_COMPLEX
color=(255,0,0)
fontscale=1.0
thickness=2
cv2.putText(canvas,"THE DEATHLY HALLOWS",(100,400),font,fontscale,color,thickness,cv2.LINE_AA)

cv2.imshow("canvas",canvas)
cv2.waitKey(0)