import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#create DataFrame
scores = pd.DataFrame({'first_name' : ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 'last_name' : ['Miller', 'Jacobson', 'Ali',
                       'Milner', 'Cooze'], 'age' : [ 42, 52, 36, 24, 73], 'female' : [0, 1, 1, 0, 1], 'preTestScore' : [ 4,24,31,2,3], 'postTestScore' : [ 25, 94, 57, 62, 70]})
print(scores)

# Create a Scatterplot of preTestScore and postTestScore,with the size of each point determined by age¶
x = scores.preTestScore
y = scores.postTestScore
s = scores.age
plt.scatter(x,y,s)
plt.xlabel('preTestScore')
plt.ylabel('postTestScore')
#plt.show()

# Create a Scatterplot of preTestScore and postTestScore.
# This time the size should be 4.5 times the postTestScore and the color determined by sex
x = scores.preTestScore
y = scores.postTestScore
colors = scores.female.apply(lambda x : 'red' if x == 1 else 'blue')
s = 4.5*(scores.age)
plt.scatter(x,y,s, c=colors)
plt.xlabel('preTestScore')
plt.ylabel('postTestScore')
plt.show()

