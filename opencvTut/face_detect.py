import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 



resourcesFolder = "Resources\\"
img = cv.imread(resourcesFolder+'\\Photos\\lady.jpg')
cv.imshow('person', img)

cv.waitKey(0) # wait for delay for key