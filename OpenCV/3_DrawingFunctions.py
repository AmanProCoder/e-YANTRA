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
cv2.imshow("canvas",canvas)
cv2.waitKey(0)


# Draw rectangle cv2.rectangle()
pt1=(200,200)
pt2=(300,300)
thickness=3

canvas=cv2.rectangle(canvas,pt1,pt2,color,thickness)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)


# Draw circle - cv2.circle()
pt=(250,250)
radius=70
color=(255,0,0)

canvas=cv2.circle(canvas,pt,radius,color,thickness)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)
