import cv2 as cv

# "C:\school\fydp\opencvTut\opencv-course\Resources\Photos\cat.jpg"
resourcesFolder = "Resources\\"
#img = cv.imread(resourcesFolder+'\\Photos\\cat.jpg')
#img = cv.imread(resourcesFolder+'\\Photos\\cat_large.jpg') # goes off screen 

#cv.imshow('Cat',img) # display image 
#cv.waitKey(0) # wait for delay for key 
# videos

capture = cv.VideoCapture(resourcesFolder +"Videos\\dog.mp4" ) # int 0 for webcam

while True:
    isTrue, frame = capture.read()
    cv.imshow("video",frame)

    if(cv.waitKey(20) & 0xFF == ord('d')): # exit cond, d pressed
        break
    # neg 215, couldn't find frames, or couldn't find more frames
capture.release()
cv.destroyAllWindows()
