import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 

# classifier face detect, algo detect +/-, 
# haarcascade + local binary: more advanced, not covered
# haarcascade on opencv has open to ppl
resourcesFolder = "Resources\\"
img = cv.imread(resourcesFolder+'\\Photos\\group 1.jpg')
cv.imshow('group 5', img)

#face detection uses edges so color not needed
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haarcascade = cv.CascadeClassifier(resourcesFolder+'haar_face.xml')
# mod scalefactor and min neighbors, to improve opencv, 
faces_rect = haarcascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 2) 
# hash cord of faces
print(f'numfaces = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w,y+h), (0,255,0), thickness=2)
cv.imshow('detectedFaces', img)

cv.waitKey(0) # wait for delay for key