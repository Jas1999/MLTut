import cv2 as cv
import numpy as np 
# "C:\school\fydp\opencvTut\opencv-course\Resources\Photos\cat.jpg"
resourcesFolder = "Resources\\"

# smooth for removing noise, from camera or other issue
img = cv.imread(resourcesFolder+'\\Photos\\cats.jpg')

# mask needs to be same size
blank = np.zeros(img.shape[:2], dtype= 'uint8')


cv.imshow('park',img) # display image 
# about color channels : b,r,g can split into individual
blank = np.zeros(img.shape[:2], dtype ='uint8')

# kernel/window, matrix : over portion of image 
# kernel size, rows and columns, bluring doing taking surrounding pixels 

#avg
# define pixel intensity using outside pixels and window slides for all pixels 
avg = cv.blur(img, (7,7)) # larger kernel more blur
cv.imshow('avg blur', avg)

# gauss blur, weighted avg give intensity, more natural and lower blur
gauss =  cv.GaussianBlur(img, (7,7), 0)
cv.imshow('gauss blur', gauss)

# median blur : more effective  at removing noise, 
median = cv.medianBlur(img,7) # assumes sq kernel
cv.imshow('median blur', median)

# bluring, retains edges 
# larger values for sigmas leads to more smudging, makes it similar to median 
biLat =  cv.bilateralFilter(img, 10, 35, 25) # img, diameter, sigmacolor : num colors considered, spaceSigma : pixel distance effect on it 
cv.imshow('biLat blur', biLat)

cv.waitKey(0) # wait for delay for key 
