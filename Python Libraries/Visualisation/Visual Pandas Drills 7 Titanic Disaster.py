import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_table('/home/becode/data/pandas/train.csv', sep=',')
print(titanic.head(10))
#Set PassengerId as the index
titanic = titanic.set_index('PassengerId')
print(titanic.head(5))
"""
#  Create a pie chart presenting the male/female proportion¶
labels = ['female','male']
femFrac = titanic.Sex[titanic.Sex == 'female'].count()
maleFrac = titanic.Sex[titanic.Sex == 'male'].count()
# only checking above results: print(titanic.groupby('Sex')['Sex'].value_counts())
fractions = [femFrac, maleFrac]
explode = (0, 0.1) # pie chart counts counter-clockwise so male part will jump out of pie by  0.01
plt.pie(fractions, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.title('Sex Proportion')
#plt.show()

# Create a scatterplot with the Fare payed and the Age, differ the plot color by gender
x = titanic.Age
y = titanic.Fare
colors = titanic.Sex.apply(lambda x : 'red' if x == 'female' else 'blue')
 #print(colors.unique())
sex = ['female','male']
plt.scatter(x,y,s=5, c=colors)
plt.xlabel('Age')
plt.ylabel('Fare')
plt.legend(title = "Sex", labels = ['female','male'])
plt.title('Scatter Fare : Age')
plt.show()

#How many people survived?
print(titanic.Survived.sum())
"""
# Create a histogram with the Fare payed
print(titanic.Fare.value_counts()) # there are 248 different fares so let's plot these vs their count in a histogram
print(titanic.Fare.unique()) # also lists 248 elements
#print(titanic.Fare.max()) # check the high value in plot
Fares = titanic.Fare.unique()
plt.hist(Fares , bins= 25, rwidth=0.95)
plt.xlabel('Fare')
plt.ylabel('Occurences')
plt.show()

