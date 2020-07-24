import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")

wine = pd.read_table('/home/becode/data/pandas/wine.data', sep =',')
print(wine.head(10))


# Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns #ERROR IN GITHUB, THEY DELETED THE WRONG ONE
#YOU Could also do it with a dictionary : col_dict = {x: col for x, col in enumerate(df.columns)} then df = df.drop(col_dict[0], 1)
wine = wine.drop([wine.columns[0],wine.columns[3],wine.columns[6],wine.columns[8],wine.columns[10],wine.columns[12],wine.columns[13]],axis=1)
print(" \n Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns : \n", wine)
# FOR ROWS # Drop a row by index df.drop([0, 1]) deletes two rows

# Assign the columns as below: alcohol, malic_acid, alcalinity_of_ash, magnesium, flavanoids, proanthocyanins, hue
wine.columns = ['alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'hue']
print(" \n Assign the columns as below: alcohol, malic_acid, alcalinity_of_ash, magnesium, flavanoids, proanthocyanins, hue : \n", wine)

# Set the values of the first 3 rows from alcohol as NaN
wine.loc[:2,'alcohol'] = np.nan
print("Set the values of the first 3 rows from alcohol as NaN : \n",wine)

# Now set the value of the rows 3 and 4 of magnesium as NaN
wine.loc[2:3,'magnesium'] = np.nan
print("set the value of the rows 3 and 4 of magnesium as NaN : \n", wine.magnesium.head(10)) #otherwise I can't see the changes..displaying datframes in Pycharm is not so amazing

# Fill the value of NaN with the number 10 in alcohol and 100 in magnesium
#wine.alcohol=wine.alcohol.replace(np.nan, 10)
#wine.magnesium=wine.magnesium.replace(np.nan, 100)
# OR to specifically change it in both mentioned columns :
#wine = wine.replace({'alcohol' : np.nan, 'magnesium' : np.nan}, 10)
#BUT THIS IS HOW IT IS BEST DONE?: INPLACE = TRUE MEANS THAT THE CHANGES ARE ACTUALLY DONE IN THE DATAFRAME
wine.alcohol.fillna(10, inplace = True)
wine.magnesium.fillna(100, inplace = True)
print("Fill the value of NaN with the number 10 in alcohol and 100 in magnesium : \n", wine)

# Count the number of missing values # this leans counting NaN!!!!!!!!!!!!
print(" \n  number of missing values : \n", wine.isnull().sum()) # this prints the count per column!!!

#  Create an array of 10 random numbers up until 10
np.random.seed(0)
randten = np.random.randint(10,size=10)
print(" \n  Create an array of 10 random numbers up until 10 : \n",randten)

# Use random numbers you generated as an index and assign NaN value to each of cell # BADLY WORDED QUeSTION, from the result they added I can see that they mean as index for rows in first column
for i in randten:
    wine.iloc[i, 0] = np.nan
print(" \n  add NaN to index row first column based on array: \n",wine.head(10))

# How many missing values do we have?
print(" \n  number of missing values : \n", wine.isnull().sum())

# Delete the rows that contain missing values # means again Nan
wine = wine.dropna(axis=0)
print(" \n  Delete the rows that contain missing values, NaN : \n",wine)


# Print only the non-null values in alcohol
print("\n only the non-null values in alcohol : \n ", wine.alcohol.notna())
print("\n only the non-null values in alcohol, the actual values : \n ", wine.alcohol[wine.alcohol.notna() == True])

# Reset the index, so it starts with 0 again
wine = wine.reset_index()
print(" \n  reset_index after deleting rows a bit back : \n", wine)
