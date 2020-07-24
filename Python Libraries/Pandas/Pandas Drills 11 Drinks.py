import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")

drinks = pd.read_table('/home/becode/data/pandas/drinks(drill11).csv', sep =',')
print(drinks.head(5))

# Return the index
print("\n Return the index: \n", drinks.index)

#  WTF!!! Identify what rows you are working with ?? I am completely lost for words..no idea what the f*uck this means..but I can see from the guidelines that he only displays European countries so..
print("\n only European countries..this was a weird question: \n", drinks[drinks.continent == 'Europe'])

# Use .loc method to retrieve an element/cell
print("\n Use .loc method to retrieve an element/cell: \n", drinks.loc[4,'total_litres_of_pure_alcohol'])

# Use .iloc method to retrieve an element/cell
print("\n Use .iloc method to retrieve an element/cell: \n", drinks.iloc[4,5])

# Set the index to 'country'
drinks = drinks.set_index('country')
print("\n Set the index to 'country: \n", drinks.head(5))

# Set a more complex index
# TRY LATER WITH MULTI-INDEX


#  Clear index name
# drinks.index.name = '' DOES THE JOB
# df_org.rename(columns={'A': 'a'}, index={'ONE': 'one'}, inplace=True) THIS IS REALLY HELPFUL
drinks = drinks.rename( index={'country' : ''})
print("\n Clear index name: \n", drinks)

#  Reset index name
drinks.index.name = 'country'
print("\n Reset index nam: \n", drinks)

# Use the index to select values from series
#print(drinks.groupby('continent')['continent'])#iloc[1])

# Sort based on values in the Series