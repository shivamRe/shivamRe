import cv2
import numpy as np

#it will retun original as it is image
img1=cv2.imread("path",-1)

#it will retun colored as it is image
img2=cv2.imread("path",1)

#it will return Gray scale image
img3=cv2.imread("path",0)

#it will return blur image
blur=cv2.GaussianBlur(img3,(21,21),0,0)

#pencile sketch of image(dividing the gray img to blur image)
img4=cv2.divide(img3,blur,scale=250)

#invert the image = 255- img
"""
#Flip the Image
img1=cv2.flip(img1,-1) #0,-1,1 can be used as paramter (it will flip the image)

#Resize the image
img1=cv2.resize(img1,(1280,700)) #Width and Height
"""

#image is the collection of pixcels for handeling that we use numpy lib.
#a. Grey scale image will return 2-D array because it's single channel image (there can be only two cases. grey cab be bright or less bright) img3
#b.Colored image is 3-D image (BGR). it will return 3-D array img2
#print(img1)

cv2.imshow("original(unchanged)",img1)
cv2.imshow("colored",img2)
cv2.imshow("gray",img3)
cv2.imshow("pencile sketch",img4)
cv2.imshow("Blur",blur)

#waitKey hold the screen for a given time
cv2.waitKey(9000)
"""
k=cv2.waitKey(0)
#When u will press s then it will close everthing
if k==ord("s"):
#it will save the image in the given location
    cv2.imwrite("path",img2)
else:
    cv2.destroyAllWindows()
"""
#You have to relase all memory after complition of task
cv2.destroyAllWin1dows()

