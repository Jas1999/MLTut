import cv2 as cv
import numpy as np

# "C:\school\fydp\opencvTut\opencv-course\Resources\Photos\cat.jpg"
resourcesFolder = "Resources\\"
 

img = cv.imread(resourcesFolder+'\\Photos\\park.jpg') # 
cv.imshow('park',img) # display image  

# rgb img to gray scale, see intensity of pixels

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Graypark',gray) # display image  

# blur image, to reduce noise 
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT ) # increase by increasing kernel
cv.imshow('blur',blur)

# edge cascade
canny = cv.Canny(blur,125,175) # reduce edges using blur, threshold values passed 
cv.imshow('canny',canny)

#dilate image
dilate = cv.dilate(canny, (3,3), iterations=3) # can apply multi iter, diff in features 
cv.imshow('dil', dilate)

#eroding image
eroded = cv.erode(dilate, (3,3), iterations=3) # can edges to get back to edge cascade from dilate
cv.imshow('eroded', eroded)

#resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) # resize ignore aspect ration, interpolation : inter_area shrink, inter_cubic enlarge
cv.imshow('resize', resize)

# cropping
# slicing image
cropped = img[50 :200,200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0) # wait for delay for key 
