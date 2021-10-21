import cv2 as cv
import numpy as np

# "C:\school\fydp\opencvTut\opencv-course\Resources\Photos\cat.jpg"
resourcesFolder = "opencv-course\\Resources\\"
#img = cv.imread(resourcesFolder+'\\Photos\\cat.jpg')
# draw on img or blank 
blank = np.zeros((500,500,3), dtype='uint8') # h,w, color channels
#img = cv.imread(resourcesFolder+'\\Photos\\cat.jpg') # goes off screen 


cv.imshow('blank',blank) # display image 
#1. paint  image a certain color or point 
#blank[:] = 0,255,0 #0,0,255 #red
#blank[200:300,300:400] =  0,0,255 #red
#cv.imshow('green',blank) # display image 

# 2. draw rect
#thickness = cv.FILLED or -1
# size (blank.shape[1]//2 , blank.shape[0]//2)
cv.rectangle(blank,(0,0), (250,250), (0,255,0), thickness = 2) # origin, size, color thickness
#cv.imshow('rectangle',blank) # display image

# 3. draw a circle
cv.circle(blank,(blank.shape[1]//2 , blank.shape[0]//2),40,(0,0,255), thickness = 2)
#cv.imshow('circle',blank)  

# 4. draw a line
# start and end points 
cv.line(blank,(100,300),(blank.shape[1]//2 , blank.shape[0]//2),
            (255,255,255), thickness = 3)
cv.imshow('line',blank) 

# 5. text on a image
cv.putText(blank, "helloworld", (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow('text',blank) 

cv.waitKey(0) # wait for delay for key 

 