import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

from sklearn.model_selection import cross_validate
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_predict


df = pd.read_csv('train2.csv')
print(df.head())

# The columns we'll use to predict the target
predictors = ["Pclass", "Sex", "Age","SibSp", "Parch", "Fare",
              "Embarked","NlengthD", "FsizeD", "Title","Deck"]
target="Survived"
# Initialize our algorithm class
alg = LinearRegression()
# Generate cross validation folds
kf = KFold(n_splits=3, random_state=1)

predictions = []

for train, test in kf.split(df):
    train_predictors = (df[predictors].iloc[train,:])
    train_target = df[target].iloc[train]
    # Put the dataset in the model
    alg.fit(train_predictors, train_target)
    # Predictions on the test fold using the fitted model
    test_predictions = alg.predict(df[predictors].iloc[test,:])
    predictions.append(test_predictions)

predictions = np.concatenate(predictions, axis=0)
predictions_list = np.array(predictions)

for i in range(0,len(predictions_list)):
    predictions_list[i] = 1 / (1 + math.exp(-1 * predictions_list[i]))
match = 0
unmatch = 0
for i in range(0,len(predictions_list)):
    if(df['Survived'].iloc[i] == 0):
        if(predictions_list[i] < 0.5):
            match = match + 1
        else:
            unmatch = unmatch + 1
    else:
        if(predictions_list[i] > 0):
            match = match + 1
        else:
            unmatch = unmatch + 1

accuracy = match/(match+unmatch)
print("Log Reg")
print(accuracy)

#LogisticRegression
lr = LogisticRegression(random_state=1)
cv = ShuffleSplit(n_splits=10, test_size=0.3, random_state=50)
#Accuracy on all cross validation folds
scores = cross_val_score(lr, df[predictors],df["Survived"],scoring='f1', cv=cv)
# Mean of all the results for every fold
print("log Reg + cross_val")
print(scores.mean())

#RandomForestClassifier
rf = RandomForestClassifier(random_state=1, n_estimators=10, min_samples_split=2, min_samples_leaf=1)
kf = KFold( n_splits=5, random_state=1)
cv = ShuffleSplit(n_splits=10, test_size=0.3, random_state=50)

predictions = cross_val_predict(rf, df[predictors],df["Survived"],cv=kf)
predictions = pd.Series(predictions)
scores = cross_val_score(rf, df[predictors], df["Survived"],scoring='f1', cv=kf)
print("RandomForestClassifier")
print(scores.mean())
