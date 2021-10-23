import cv2 as cv
import numpy as np 
# "C:\school\fydp\opencvTut\opencv-course\Resources\Photos\cat.jpg"
resourcesFolder = "Resources\\"


img = cv.imread(resourcesFolder+'\\Photos\\park.jpg')
cv.imshow('park',img) # display image 
# about color channels : b,r,g can split into individual
blank = np.zeros(img.shape[:2], dtype ='uint8')

b,g,r = cv.split(img)
cv.imshow('b', b) # show kinda gray scale w pixel density, more of a color means more of a color, less darker
cv.imshow('g', g)
cv.imshow('r', r)

print(img.shape) # img size and color channel
print(b.shape)# just size
print(g.shape)
print(r.shape)

m =  cv.merge([b,r,g])
cv.imshow('m', m)
 
blue  = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red   = cv.merge([blank,blank,r])
#better dist of images by showing darker lighter were less, can still merge
cv.imshow('blue', blue) # show kinda gray scale w pixel density, more of a color means more of a color, less darker
cv.imshow('green', green)
cv.imshow('red', red)


cv.waitKey(0) # wait for delay for key 
