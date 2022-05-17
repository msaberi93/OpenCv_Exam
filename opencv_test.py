import cv2

img = cv2.imread("C:/Users/MSaberi/Desktop/image1.jpg" , 1)
# imgb = cv2.line(img, (600,100),(200,200),(255,0,0) , 5)
# imgR = cv2.rectangle(img,(100,200),(400,950),(0,0,255),3)
# imgG = cv2.circle(img,(310,500),250,(0,255,0),4)
# imgG = cv2.circle(img,(910,900),350,(0,255,0),-1,4)
# imgE = cv2.ellipse(img,(925,100),(80,30),0,0,250,100,5,-1)

# img1 = cv2.imread("c:/Users/MSaberi/Desktop/image1.jpg" , 1)
# img2 =  cv2.imread("c:/Users/MSaberi/Desktop/image1.jpg" , -1)

import numpy as np
pts = np.array([[80,150],[100,30],[120,60],[50,90]])
imgP = cv2.polylines(img,[pts],True,[0,0,0])

#cv2.namedWindow('image_AUTOSIZE',cv2.WINDOW_AUTOSIZE)
#cv2.imshow('img',img)
#cv2.namedWindow('image_AUTOSIZE',cv2.WINDOW_AUTOSIZE)
#cv2.imshow('img1',img1)
#cv2.namedWindow('image_AUTOSIZE',cv2.WINDOW_AUTOSIZE)
#cv2.imshow('img2',img2)

cv2.imwrite("img.jpg" , img)
cv2.imwrite("imgP.jpg" , imgP)
# cv2.imwrite("imgG.jpg" , imgG)

# cv2.imwrite("img1.jpg" , img1)
# cv2.imwrite("img2.jpg" , img2)

