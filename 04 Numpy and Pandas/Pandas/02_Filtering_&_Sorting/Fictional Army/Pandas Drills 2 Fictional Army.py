import numpy as np
import pandas as pd

army = pd.DataFrame({'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']})

print(army)
print(" \n set origin as index column: \n") # WATCH OUT ARMY = ARMY.set_index()
army = army.set_index('origin')
print(army)
print(" \n print only veterans: \n", army.veterans)
print(" \n print only veterans and deaths : \n", army[['veterans', 'deaths']])
print(" \n print list columns : \n", army.columns.tolist())
print(" \n 'deaths', 'size' and 'deserters' from Maine and Alaska: \n", army.loc[['Maine', 'Alaska'], ['deaths', 'size' ,'deserters']]) # works like this because
# Maine and Alsaska are in index column
print(" \n rows 3 to 7 and the columns 3 to 6: \n", army.iloc[2:7, 2:6])
print(" \n every row after the fourth row and all columns: \n", army.iloc[4:, :])
print(" \n every row up to the 4th row and all columns: \n", army.iloc[0:4, :])
print(" \n the 3rd column up to the 7th column: \n", army.iloc[:, 2:7])
print(" \n rows where df.deaths is greater than 50: \n", army[army.deaths > 50])
print(" \n rows where df.deaths is greater than 500 or less than 50: \n", army[(army.deaths > 500) | (army.deaths < 50) ])
print(" \n all the regiments not named 'Dragoons': \n", army[army.regiment != 'Dragoons'])
print(" \n rows called Texas and Arizona: \n", army.loc[['Texas','Arizona'], :]) # omdat index in Origin kan ik dit zo doen
print(" \n rows called Texas and Arizona, the REAL solution: \n", army.loc[ ['Arizona','Texas']])
print(" \n row called Texas : \n", army.loc[['Texas']])
#print(" \n the third cell in the row named Arizona: \n", army.loc[['Arizona']])
#print(" \n the third cell in the row named Arizona: \n", army[army['origin'] == 'Arizona'].iloc[:,2:3])
                                          #               army[army['origin'] == 'Arizona'].iloc[:,2:3]
#print(" \n the third cell down in the column named deaths: \n", army['deaths'].iloc[2:3,:])
#print(army.at['3','deaths'])