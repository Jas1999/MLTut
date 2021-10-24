import os
import cv2 as cv
import numpy as np
resourcesFolder = "Resources\\"
DIR = resourcesFolder+"Faces\\train"
ppl = []
for i in os.listdir(DIR):
    ppl.append(i)
print(ppl)

features = [] # img arrays of faces
labels = [] # labels relating 
haarcascade = cv.CascadeClassifier(resourcesFolder+'haar_face.xml')

def create_train(): 
    for person in ppl:
        path  =  os.path.join(DIR,person)
        label = ppl.index(person)

        for img in os.listdir((path)):
            img_path = os.path.join(path,img)

            img_arr =  cv.imread(img_path)
            gray = cv.cvtColor(img_arr,cv.COLOR_BGR2GRAY)

            faces_rect =  haarcascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label) # storing index 

create_train()
print('features len ', len(features))
print('labels len ', len(labels) )

# now face recog

face_recognizer = cv.face.LBPHFaceRecognizer_create()
# train recognizer w features and lists, need as numpy list first 

features = np.array(features,dtype='object') # img arrays of faces
labels = np.array(labels) # labels relating 

face_recognizer.train(features,labels) # trained and use,  but need to add images again if want to use in another file 
# save features and face recogn

face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)




