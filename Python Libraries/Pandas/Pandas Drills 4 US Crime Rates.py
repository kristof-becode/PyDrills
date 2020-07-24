import numpy as np
import pandas as pd

crime = pd.read_table('/home/becode/data/pandas/US_Crime_Rates_1960_2014.csv', sep=',')
print(crime)
print("\n column dtypes : \n ", crime.dtypes)
#crime.Year = crime.Year.astype('datetime64[ns]') # 'datetime64[ns]' !!!!!!!!! gives something weird, better use pd.to_datetime see below
crime.Year = pd.to_datetime(crime.Year, format='%Y')
print("\n check dtypes to see 'Year' dtype is altered : \n ", crime.dtypes)
crime = crime.set_index('Year')
#print(crime.index)
print("\n nu met 'Year' als index : \n ",crime.head(10))
print("\n drop 'Total' column : \n ")
crime = crime.drop('Total', axis = 1)
print(crime)
#crime = crime.groupby([(crime.index.year//10)*10 , crime.Population == crime.Population.max()]).sum() #max()] # TOO FUNKY RESULT
crime = crime.groupby([(crime.index.year//10)*10]).sum()
#crime = crime.groupby([(crime.index.year//10)*10])[crime.Population.max()].sum()#max()#.sum() #max()]
print(crime)
#print("\n Group the year by decades and sum the values : \n ",crime.groupby('Year').sum()) #Pay attention to the Population column number, summing this column is a mistake
#print("\n Group the year by decades and sum the values : \n ",crime.groupby(crime.index.year //10 * 10)) #.sum())
#print("\n Group the year by decades and sum the values : \n ",crime.groupby[crime.index = crime.index.year.apply(lambda x : x//10 * 10)]) #.sum())
#crime.Year = crime.Year.apply(lambda x : x // 10 * 10)
#print(crime.groupby(crime.Year = crime.Year.apply(lambda x : x // 10 * 10)).sum())
#df.index.year//10)*10
#DateTimeIndex.year.apply(lambda x : x // 10 * 10) #.sum())
#print(crime)
#crime = crime.groupby