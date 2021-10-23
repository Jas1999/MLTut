import cv2 as cv
import numpy as np 
 
blank  = np.zeros((400,400), dtype = 'uint8')
rect = cv.rectangle(blank.copy(), (30,30), (370,370), 255,-1)
circle = cv.circle(blank.copy(), (200,200), 200, 255,-1)

cv.imshow('rect',  rect)
cv.imshow('circle',circle)

# bitwise and
bw_and = cv.bitwise_and(rect, circle)
cv.imshow('and',bw_and) # overlapping show only -- intersecting
# or
bw_or = cv.bitwise_or(rect, circle)
cv.imshow('or',bw_or) # all , non + intersecting
# xor
bw_xor = cv.bitwise_xor(rect, circle)
cv.imshow('bw_xor',bw_xor) # non intersecting 

# bitwise not : inverts binary color for all, ie black to white
bitwise_not =  cv.bitwise_not(rect)
cv.imshow('bitwise_not',bitwise_not) # non intersecting 


cv.waitKey(0) # wait for delay for key 
