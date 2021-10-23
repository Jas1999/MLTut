import cv2 as cv
import numpy as np 
 
# use bitwise to focus on parts of ig
resourcesFolder = "Resources\\"
img = cv.imread(resourcesFolder+'\\Photos\\cats.jpg')
cv.imshow('cats', img)

# mask needs to be same size
blank = np.zeros(img.shape[:2], dtype= 'uint8')
cv.imshow('blank', blank)

rect = cv.rectangle(blank.copy(), (30,30), (370,370), 255,-1)
cv.imshow('rect', rect)


mask = cv.circle (blank,(img.shape[1]//2+45,img.shape[0]//2),100,255,-1 )
cv.imshow('mask', mask)

weirdshape = cv.bitwise_and((mask), rect)
cv.imshow('weirdshape', weirdshape)

masked = cv.bitwise_and(img, img, mask = weirdshape)
cv.imshow('masked', masked)

cv.waitKey(0) # wait for delay for key 
