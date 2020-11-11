import numpy as np
import pandas as pd

drinks = pd.read_table('/home/becode/data/pandas/drinks.csv', sep =',')
print(drinks)
print("\n Which continent drinks more beer on average : \n ", drinks.groupby('continent')['beer_servings'].mean())
print("\n For each continent print the statistics for wine consumption:\n", drinks.groupby('continent')['wine_servings'].describe())
print("\n Print the mean alcohol consumption per continent for every column:\n", drinks.groupby('continent').mean())
print("\n Print the median alcohol consumption per continent for every column:\n", drinks.groupby('continent').median())
print("\n Print the mean, min and max values for spirit consumption and print out DataFrame:\n", drinks.groupby('continent').median())
#print(drinks.groupby('continent')['spirit_servings'].max())
new = pd.DataFrame({'mean' : drinks.groupby('continent')['spirit_servings'].mean(), 'min' : drinks.groupby('continent')['spirit_servings'].min(), 'max' : drinks.groupby('continent')['spirit_servings'].max()})
print(new)
# !!!!!! complex : I had to delete a first column where I tried to put the continents, only then I saw that he places that column itself, probably because of the groupby!!!!!!