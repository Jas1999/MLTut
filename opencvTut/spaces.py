import cv2 as cv

#switch color spaces 
resourcesFolder = "Resources\\"
img = cv.imread(resourcesFolder+'\\Photos\\park.jpg') 
cv.imshow('park',img)

# bgr to grayscale
gray =  cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# bgr to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab',hsv)

# bgr is reverse of colors, everything other than opencv is rgb 
# ie inverted in matplotlib

# bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB) # shows inversion since opencv is inverting it, if u pass rgb to mathplot lib it shows up normally
cv.imshow('rgb', rgb)

#bgr is the middle, if you want another conversion ie gray to lab

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('h_b',hsv_bgr)

lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('l_b',lab_bgr)


cv.waitKey(0)
