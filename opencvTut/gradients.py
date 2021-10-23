import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 
# grad and edge detection :
# similar prog prospective, 
resourcesFolder = "Resources\\"
img = cv.imread(resourcesFolder+'\\Photos\\park.jpg')
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Laplacian
lap = cv.Laplacian((gray), cv.CV_64F)
lap =  np.uint8(np.absolute(lap)) # abs since gray to black negative slope, but need positive for pixels
cv.imshow('Laplac',lap) # most edges are covered

#sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0) # direction spec grad, over y,so vertical ones 
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
comb = cv.bitwise_or(sobelx, sobely)

# canny

canny = cv.Canny(gray,150,175)
cv.imshow('canny', canny)
# diff algo and diff result
# sobel gradients --> more advanced cases 
# laplace shaded version  
# canny uses sobel and just lines, cleaner for edges --> used often


cv.imshow('sobelx',sobelx) # most edges are covered
cv.imshow('sobely',sobely) # most edges are covered
cv.imshow('comb',comb) # most edges are covered


cv.waitKey(0) # wait for delay for key 
