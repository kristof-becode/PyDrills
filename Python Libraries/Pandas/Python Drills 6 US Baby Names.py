import numpy as np
import pandas as pd

baby_names = pd.read_table('/home/becode/data/pandas/US_Baby_Names_right.csv', sep =',')

# See the first 10 entries
print("\n See the first 10 entries : \n",baby_names.head(10))

# Delete the column(s) 'Unnamed: 0' and 'Id'
baby_names = baby_names.drop(columns=['Unnamed: 0', 'Id']) # OR baby_names.drop(['Unnamed: 0', 'Id'], axis=1)
print(baby_names.head(10))

# Is there more male or female names in the dataset? # MORE FEMALE!
print("\n Is there more male or female names in the dataset? # MORE FEMALE! \n", baby_names.Gender.value_counts())

# Group the dataset by name and assign to names
print("\n Group the dataset by name and assign to names: \n", baby_names.groupby('Name')['Name'].count())
#print("\n There are names used both for females and males a: \n", baby_names.groupby(['Name', 'Gender'])['Name'].count())

#. How many different names exist in the dataset?
#print("\n How many different names exist in the dataset: \n", baby_names.groupby('Name')['Name'].count())

# What is the name with most occurrences? Well, Jacob could be the most occuring Male name but Riley is the most occuring name regardless of Gender!!!
print("\n What is the name with most occurrences?: \n", baby_names.groupby('Name')['Name'].value_counts().max())
print("\n What is the name with most occurrences?: \n", baby_names.groupby('Name')['Name'].value_counts().idxmax())

#MALE MOST OCCURING
print("\n What is the MALE name with most occurrences?: \n", baby_names.groupby('Name')['Name'].value_counts().idxmax())
print(baby_names[baby_names.Gender == 'M'].groupby('Name')['Name'].value_counts().max())
#MALE MOST OCCURING
print("\n What is the FEMALE name with most occurrences?: \n", baby_names.groupby('Name')['Name'].value_counts().idxmax())

print(baby_names[baby_names['Name'] == 'Jacob'])
print(baby_names[baby_names['Name'] == 'Riley'])


# How many different names have the least occurrences?
print("\n What is the name with least occurrences?: \n", baby_names.groupby('Name')['Name'].value_counts().min())


# What is the median name occurrence?
print("\n What is the median name occurrence?: \n", baby_names.groupby('Name')['Name'].value_counts().median())


# What is the standard deviation of names?
print(baby_names.groupby('Name')['Name'].value_counts().describe())



#Get a summary with the mean, min, max, std and quartiles.
