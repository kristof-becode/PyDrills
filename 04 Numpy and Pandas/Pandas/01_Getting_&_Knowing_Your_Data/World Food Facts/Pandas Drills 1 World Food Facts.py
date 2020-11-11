import numpy as np
import pandas as pd

food = pd.read_table('/home/becode/data/pandas/en.openfoodfacts.org.products.tsv') # sep='|')
print(" \n first 5 : \n",food.head(5))
print(" \n number observations with food.shape : \n",food.shape)
print(" \n number of rows with food.shape[0] : \n",food.shape[0])
print(" \n number of columns with food.shape[1] : \n",food.shape[1])

print(" \n list columns with .columns.tolist() : \n", food.columns.tolist())
print(" \n list columns with list(food.columns) : \n",list(food.columns))
# 3 WAYS OF PRINTING COLUMN 105
print(" \n printing 105th column in several ways \n")
count = 0
for col in food.columns:
    count += 1
    if count ==105:
        print(col)
print(list(food.columns)[104]) # index 104 is 105-th element
print(food.columns[104]) # also works

print(" \n ? how indexed \n" , food.index)
print(" \n ? type of 105th columns via food[food.columns[104]].dtype  \n" ,food[food.columns[104]].dtype)
print(" \n ? product name for 19th observation \n" ,food.product_name[18]) # product_name for 19th observation or row 19