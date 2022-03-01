import cv2
import time
import numpy as np

#Open the Camera (DSHOW for preventing the warning  # passing 0 for internal web cam and 1 for external camera by using ip address)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#SAVE VIDEO in XVID format and save at location  , format can be DIVX ,XVID, MJPG X264, WMV1, WMV2
fourcc=cv2.VideoWriter_fourcc(*"XVID")
#it contain 4 parameter ,name,codec,fps,resolution
output=cv2.VideoWriter("Path where u want to store your output",fourcc,20.0,(640,480),0)
print(cap)
# it will check for camera is it open or not and do the operations
while cap.isOpened():
    # ret will return boolean value and frame will return image (video is collection of image or frame)
    ret,frame=cap.read()
    if ret==True:
        #Resize the video
        resizeFrame=cv2.resize(frame,(700,450))
        #Covert video into grey color
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #Filp the video 0 or 1
        frame=cv2.flip(frame,0)
        #Show the  colored video
        cv2.imshow("FRAME", frame)
        # Show the gray video
        cv2.imshow("grey", gray)
        #save gray frame video in given location.
        output.write(gray)
    #Exit from the code press x
    if cv2.waitKey(1)& 0XFF == ord('x'):
        break
# release the caputre video
cap.release()
#release the video that mean it will save img properly
output.relase()
cv2.destroyAllWin1dows()