import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 
# thresholding, binarization, img to binary image using threshold to set pixel intensity
resourcesFolder = "Resources\\"
img = cv.imread(resourcesFolder+'\\Photos\\cats.jpg')
cv.imshow('cats', img)

# simple thresholding
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

threshold,thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # over 150 set to 255, compares each pixel
cv.imshow('Simple Threshold', thresh)

# inverse of img
threshold,thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) # over 150 set to 255, compares each pixel
cv.imshow('Simple Threshold', thresh_inv)

# adpative thresholding 
# kernel mean and threshold found for the each section

#adaptive_thresh = cv.adaptiveThreshold((gray), 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3) # mean for threshold, c minus mean for fine tuning 
# inverse by fliping thresh binary
# smaller kernal and higher sub more details 
# instead of mean using gausian : adds weights
adaptive_thresh = cv.adaptiveThreshold((gray), 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3) # mean for threshold, c minus mean for fine tuning 

cv.imshow('adaptive_thresh Threshold', adaptive_thresh)

cv.waitKey(0) # wait for delay for key 
