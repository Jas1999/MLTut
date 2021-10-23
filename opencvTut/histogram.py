import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 
# histogram : dist of pixel density : works both gray and bgr
resourcesFolder = "Resources\\"
img = cv.imread(resourcesFolder+'\\Photos\\cats.jpg')
cv.imshow('cats', img)

# mask needs to be same size
blank = np.zeros(img.shape[:2], dtype= 'uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
# gray hist, pass list or only one and pass channel
# can mask to isolate part

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow("circle",circle)

#mask = cv.bitwise_and((gray), gray,mask=circle)
mask = cv.bitwise_and((img), img,mask=circle)
cv.imshow('Mask', mask)

#gray_hist = cv.calcHist([gray], [0], mask,[256], [0,256])

plt.figure()
plt.title('color hist')
plt.xlabel('bins')
plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show() # peak color

# color hist
colors = ('b','g','r')

for i,col in enumerate(colors):
    #hist = cv.calcHist([img], [i], mask, [256], [0,256])
    hist = cv.calcHist([img], [i], circle, [256], [0,256]) # need mask for individual channel 
    plt.plot(hist,color =col)
    plt.xlim([0,256])
plt.show() # comp brg channels for each 
cv.waitKey(0) # wait for delay for key 
