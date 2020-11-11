import numpy as np
import pandas as pd

euro12 = pd.read_table('/home/becode/data/pandas/Euro_2012_stats_TEAM.csv', sep =',')
print(euro12)

print("\n only Goals : \n", euro12.Goals)
print("\n # rows : \n",euro12.shape[0])
print("\n # columns : \n",euro12.shape[1])
discipline = euro12[['Team','Yellow Cards','Red Cards']]
print("\n only certain columns, way 1 : \n",discipline)
discipline = euro12.loc[:,['Team','Yellow Cards','Red Cards']]
print("\n only certain columns, way 2 using loc : \n",discipline)
print("\n sorted first on Red then on Yellow Cards, ascending : \n",discipline.sort_values(by= ['Red Cards', 'Yellow Cards'])) # first sorted on Red then on Yellow !!!!!!
print("\n sorted first on Red then on Yellow Cards, descending : \n",discipline.sort_values(by= ['Red Cards', 'Yellow Cards'], ascending = False))
print("\n mean # Yellow Cards, rounded to one digit after comma : \n",round(discipline['Yellow Cards'].mean(),1))
print("\n Teams(but others columns too) with more than 6 goals : \n", euro12[euro12.Goals > 6]) # or euro12[euro12['Goals'] > 6]
print("\n Teams(but others columns too) that start with 'G' : \n", euro12[euro12.Team.str[0] == 'G'])
print("\n first 7 columns : \n",euro12.iloc[:, 0:7]) # if index = 7 then you print 0 to 6 which is first 7 columns!
print("\n all columns but last 3 : \n",euro12.iloc[:, :-3])
#print("\n Shooting accuracy of 3 countries : \n",euro12.loc[ ['England', 'Italy', 'Russia'] , ['Team', 'Shooting Accuracy']])
#print("\n Shooting accuracy of 3 countries : \n",euro12.loc[ ' , 'Shooting Accuracy'])
#rows = ['England', 'Italy', 'Russia']
print("\n Shooting accuracy of 3 countries : \n",euro12.loc[:, ['Team', 'Shooting Accuracy']])
print("\n Shooting accuracy of 3 countries : \n",euro12[['Team'  , 'Shooting Accuracy']])
print("\n Shooting accuracy of 3 countries : \n",euro12.loc[:, ['Team', 'Shooting Accuracy']][euro12.Team == 'England' or 'Italy' or 'Russia' ])

