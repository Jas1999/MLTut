import cv2 as cv
import numpy as np
# "C:\school\fydp\opencvTut\opencv-course\Resources\Photos\cat.jpg"
resourcesFolder = "Resources\\"
img = cv.imread(resourcesFolder+'\\Photos\\cats.jpg') 
cv.imshow('Cats',img) # display image 

blank = np.zeros(img.shape, dtype='uint8')

cv.imshow('blank',blank) # display image 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayCats',gray) # display image 


'''
blur = cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
canny = cv.Canny(blur,125,175) 
cv.imshow('cannyCats',canny) # display image 
'''
# alt is threhold, which turns anything below intensity to 0

ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY) # binarize image,0 or 1
cv.imshow('threshCats',thresh)

# contrours bind edges, usually try canny first then threshold 
#contours,hierachies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) # list all retr, external : returns ones outside, retr_tree returns in tree, 
contours,hierachies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) # list all retr, external : returns ones outside, retr_tree returns in tree, 
#apprx method for contour: simple compess lines into end points, none get all points

print(f'{len(contours)} contours found') 

cv.drawContours(blank, contours, -1, (0,0,255), 2)#
cv.imshow('con draw',blank )
cv.waitKey(0) # wait for delay for key 
# videos
 