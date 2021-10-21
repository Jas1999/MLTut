import cv2 as cv

# "C:\school\fydp\opencvTut\opencv-course\Resources\Photos\cat.jpg"
resourcesFolder = "opencv-course\\Resources\\"
#img = cv.imread(resourcesFolder+'\\Photos\\cat.jpg')
# rescale h and w to reduce info

def rescaleFrame(frame,scale=0.75):
    # img, video and live video
    w = int(frame.shape[1]*scale)
    h = int(frame.shape[0]*scale)

    d = (w,h)

    return cv.resize(frame,d,interpolation= cv.INTER_AREA)

def changeRes(w,h):
    # only live video : read external 
    capture.set(3,w)
    capture.set(4,h) #3,4 stand for w and h, brightness could be 10


img = cv.imread(resourcesFolder+'\\Photos\\cat_large.jpg') # goes off screen 
reimg = rescaleFrame(img)
cv.imshow('Cat',img) # display image 
cv.imshow('Cat resized',reimg)
#cv.waitKey(0) # wait for delay for key 

capture = cv.VideoCapture(resourcesFolder +"Videos\\dog.mp4" ) # int 0 for webcam

while True:
    isTrue, frame = capture.read()
    #cv.imshow("video",frame)
    frame_resized =  rescaleFrame(frame, scale=0.2)

    cv.imshow("video",frame)
    cv.imshow("video resize",frame_resized)
    if(cv.waitKey(20) & 0xFF == ord('d')): # exit cond, d pressed
        break
    # neg 215, couldn't find frames, or couldn't find more frames
capture.release()
cv.destroyAllWindows()