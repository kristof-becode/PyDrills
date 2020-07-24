import numpy as np
import pandas as pd

# !!!! https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html !!!!!!

# Create the 3 DataFrames based on the following raw data
raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

# Assign each to a variable called data1, data2, data3

data1 = pd.DataFrame(raw_data_1)
data2 = pd.DataFrame(raw_data_2)
data3 = pd.DataFrame(raw_data_3)
print(data1,"\n","\n", data2,"\n","\n", data3)

# Join the two (first?) dataframes along rows and assign all_data
conca1 = [data1, data2]
all_data = pd.concat(conca1,axis =0) # OR all_data = pd.concat([data1, data2],axis =0)
print("\n Join the two (first?) dataframes along rows and assign all_data : \n", all_data)
# If you want the index to be updated and not just taken over then you set as parameter : pd.concat(conca1,axis =0, ignore_index=True) !!!!!

# Join the two dataframes along columns and assing to all_data_col
all_data_col = pd.concat(conca1,axis =1)
print("\n Join the two (first?) dataframes along columns and assign all_data : \n", all_data_col)

#Print data3
print("\n Print data3 : \n", data3)

#Merge all_data and data3 along the subject_id value
merge1 = pd.merge(all_data,data3, on="subject_id")
print("\n JMerge all_data and data3 along the subject_id value(only shared fields in subject_id will make it in the merge, repetitions included) : \n",merge1)
# only shared fields in subject_id will make it in the merge, repetitions included, not shared ones will be deleted

# Merge only the data that has the same 'subject_id' on both data1 and data2
merge2 = pd.merge(data1,data2,on="subject_id")
print("\nMerge only the data that has the same 'subject_id' on both data1 and data2 : \n",merge2)

#Merge all values in data1 and data2, with matching records from both sides where available.
merge3 = pd.merge(data1,data2,on='subject_id', how='outer')
print("\n Merge all values in data1 and data2, with matching records from both sides where available : \n",merge3)

