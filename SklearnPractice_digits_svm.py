import matplotlib.pyplot as pyplot
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()
classifier = svm.SVC(gamma=0.001, C=100)
print(len(digits.data))
x,y = digits.data[:-10], digits.target[:-10] # test and sample
classifier.fit(x,y)
#-1 is last
print('Predict:', classifier.predict(digits.data[[-2]]))

pyplot.imshow(digits.images[-2],cmap=pyplot.cm.gray_r, interpolation = "nearest")
pyplot.show()
