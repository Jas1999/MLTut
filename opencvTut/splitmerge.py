import cv2 as cv
import numpy as np 
# "C:\school\fydp\opencvTut\opencv-course\Resources\Photos\cat.jpg"
resourcesFolder = "Resources\\"
img = cv.imread(resourcesFolder+'\\Photos\\park.jpg')

cv.imshow('park',img) # display image 
cv.waitKey(0) # wait for delay for key 
