import numpy as np
import pandas as pd

users = pd.read_table('/home/becode/data/pandas/u.tsv', sep='|')
users = users.set_index('user_id')
print(" \n first 25 : \n", users.head(25))
print(" \n last 10 : \n",users.tail(10))
print(" \n number of observations and columns \n")
print(users.shape)
print(" \n kolomlijst, nu zonder user_id want die is index geworden! : \n",users.columns.tolist())
print(" \n how indexed? : \n",users.index)
print(" \n column datatypes : \n",users.dtypes)
print(" \n print 'occupation' column : \n", users.occupation)
print(" \n print 'occupation' column : \n", users['occupation'])
print(" \n ? different occupations via users.occupation.value_counts().count(): \n",users.occupation.value_counts().count())
print(" \n list of diff occupations : \n", users.occupation.unique())
print(" \n ? different occupations via len(users.occupation.unique() : \n", len(users.occupation.unique()))
print(" \n most frequent occupation: \n",users.occupation.value_counts().idxmax()) # with idx I get the occupation and not its value count
print(" \n summarize dataframe users via users.describe(): \n",users.describe())
print(" \n summarize all columns dataframe users via users.describe(include='all'): \n",users.describe(include='all'))
print(" \n summarize occupation column via users.occupation.describe(): \n",users.occupation.describe())
print(" \n mean age user : \n", users.age.mean())
print("\n user age value_count : \n", users.age.value_counts())
print(" \n least frequent age : \n", users.age.value_counts()[users.age.value_counts() == users.age.value_counts().min()])

"""
#PLAYING AROUND WITH ILOC
print(users[0:3]) #print first 3 rows
print(users.iloc[0:3,:]) #print first 3 rows
print(users.iloc[0:3,0:2]) #print first 3 rows and first two columns
print(users.iloc[:,2]) # print all rows and third(index=2) column
"""