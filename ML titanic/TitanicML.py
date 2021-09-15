import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy
import math

# Continous vs Continous - Correlation
def covar(a, b):

    a_mean = numpy.mean(a) #sum(a)/len(a)
    b_mean = numpy.mean(b)
    length = len(a)
    sum = 0

    for i in range(0, len(a)):
        sum += ((a[i] - a_mean) * (b[i] - b_mean))

    return sum/length

df =  pd.read_csv("C:\\school\\coop 4\\ML titanic\\train.csv")
print(df.shape)
print(df.columns)
print(df.head())
df.describe()
df[['Age','Survived']].iloc[0:10]
# print(df.shape)
df.groupby('Survived').count()
df.sort_values('Fare')

df.hist(bins=10,grid=False)
grind = sns.FacetGrid(df, col = "Pclass", row= "Sex", margin_titles=True)
grind.map(plt.hist,"Survived")
grind.map(plt.hist,"Age")
live = df[df["Survived"] == 1]['Pclass'].value_counts()
die = df[df["Survived"] == 0]['Pclass'].value_counts()
pd.DataFrame([live,die]).plot(kind='bar', stacked =True)

s = pd.DataFrame([live,die])

print(s.iloc[0,0]) #first class alive
print(s.iloc[1,0]) #first class died

PclassTotal = s.iloc[1,0] + s.iloc[0,0]
#print(pd.DataFrame([live]))
#print(s['Pclass'].iloc[0])

pclass1_live = s.iloc[0,0]/ PclassTotal # s['Pclass1'].iloc[0]/s['Pclass1'].sum()
pclass1_live = pclass1_live*100
print("Percentage of surviving passengers from Pclass1 " + str(pclass1_live))

print("L2: " )
print(df.shape)
print(df.columns)
print(df.head())
print("Univariate analysis" )
print(df[['Age','SibSp','Fare']].describe())
df2 = df.dropna()
#sns.distplot(df2['Age'])


#df_em = df['Embarked'].value_counts()
#df_em.plot(kind='bar')
#print("Frequency of S " + str(df_em['S']/df_em.sum()))

#BiVariate Analysis
#Continous vs Continous - Scatter
from matplotlib import pyplot
pyplot.scatter(df['Fare'], df['Age'])
pyplot.show()

covariance = covar(df['PassengerId'].values, df['SibSp'].values)
print(covariance)
print(covariance/math.sqrt((numpy.var(df['PassengerId'].values)*numpy.var(df['SibSp'].values))))

x = numpy.cov(df['PassengerId'].values, df['SibSp'].values)
print(x[0][1])

#Continous vs Continous - Two Table method
df2 = df.dropna()
total = df2.shape[0]
cols = df2['Embarked'].unique()
rows = df2['Survived'].unique()
print(cols)
print(rows)
table = []
for i in rows:
    curr = []
    for j in cols:
        df2 = df
        df2 = df2[df2['Embarked'] == j]
        df2 = df2[df2['Survived'] == int(i)]
        count = df2.shape[0]
        curr.append(count)
    table.append(curr)
print(table)

#Data Cleaning
#Drop Duplicates
print("clearning")


df2 = df.drop_duplicates();
print(df2.shape[0] - df.shape[0])
df2 = df.drop_duplicates(subset=['Age','Fare']);
print(df2.shape[0] - df.shape[0])


df2 = df.loc[df['Embarked'].isnull()]
print(df2.shape)
df2.head()

sns.boxplot(x="Embarked", y="Fare", hue="Pclass", data=df);

df["Embarked"] = df["Embarked"].fillna('C')

df2 = df.loc[df['Age'].isnull()]
df2.head()

#Median
print("med")

df3 = df.dropna(axis=0, how = 'any')
print(df3['Age'].median())
df3 = df3.loc[df3['Fare'] >= 6]
df3 = df3.loc[df3['Fare'] <= 10]
print(df3['Age'].median())


df2 = df.loc[df['Cabin'].isnull()]
df2.head()


# Most Frequent
print("freq")

df2 = df.dropna(axis=1,how='any')
df2 = df.loc[df['Pclass'] == 3]
df2 = df2.loc[df2['Embarked'] == 'S']
df2['Cabin'].value_counts()


# Interpolation
print("inter")
s = pd.Series([0, 1, numpy.nan, 3])
print(s)
s.interpolate(method='linear',inplace=True)
print(s)
