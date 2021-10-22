import cv2 as cv
import numpy as np
# "C:\school\fydp\opencvTut\opencv-course\Resources\Photos\cat.jpg"
resourcesFolder = "Resources\\"
img = cv.imread(resourcesFolder+'\\Photos\\park.jpg')

cv.imshow('park',img) # display image 

#Translations
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    d = (img.shape[1],img.shape[0])

    return cv.warpAffine(img,transMat,d)
# - x ==> left
# - y ==> up 

translated = translate(img,100,100)
cv.imshow('translated_park',translated) # display image 

#rotation : by angle
def rotate(img,angle,rotPoint = None):
    (h,w) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (w//2,h//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    d = (w,h)

    return cv.warpAffine(img,rotMat,d)

rotated = rotate(img,-45) # can apply func again -- would do the rotated img not the original, so bars 
cv.imshow("rot", rotated)

# resize image
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resize", resize)

#flipping 
flip=cv.flip(img,0) # 0 flip x, 1 on y, -1 both  
cv.imshow("flip", flip)

#cropping
cropped = img[200:400,300:400]
cv.imshow("cropped", cropped)

cv.waitKey(0) # wait for delay for key 
