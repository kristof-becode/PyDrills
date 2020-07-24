import numpy as np
import pandas as pd

df = pd.read_table('/home/becode/data/pandas/chipotle.tsv')
# or = pd.read_csv('/home/becode/data/pandas/chipotle.tsv', sep='\t')

chipo = df
print(chipo.head(10))
print(chipo.shape)
print("columns :", chipo.shape[0])
print("rows :",chipo.shape[1])
print(chipo.describe)
print("list columns : \n", chipo.columns.tolist())
#indexed per purchase, several witj index 1 are for first purchase
print("? indexed how : \n", chipo.index)
print(" \n VALUE COUNTS ITEM_NAME : \n", chipo['item_name'].value_counts()) # is again a dataframe so I can do same manipulations
print(" \n NUMBER OF ORDERS FOR MOST ORDERED ITEM : \n", (chipo['item_name'].value_counts()).max()) # gives number of max occurences, max buys
print("MOST ORDERED ITEM: \n", (chipo['item_name'].value_counts()).idxmax()) # gives item_name with max buys
print("VALUE COUNTS FOR DESCRIPTION_CHOICE: \n",chipo['choice_description'].value_counts()) # dataframe value_counts for choice_description
print(" \n NUMBER OF ORDERS FOR MOST ORDERED ITEM iN DESCRIPTION_CHOICE : \n", chipo['choice_description'].value_counts().max())
print(" \n MOST ORDERED ITEM iN DESCRIPTION_CHOICE : \n", chipo['choice_description'].value_counts().idxmax())
print(" \n dtypes for columns : \n",chipo.dtypes)
print(" \n dtype for column item_price : \n",chipo['item_price'].dtype)
#chipo['item_price'].apply(lambda str : str.replace({'$', ''})) #str.replace(r'\D', '').astype(float64)
chipo['item_price'] = chipo['item_price'].apply(lambda str : str[1:])
print(" \n column item_price, dollar sign is removed,check : \n", chipo['item_price'])
chipo['item_price'] = chipo['item_price'].astype('float64')
print(" \n check dtype item_price is float64 : \n", chipo['item_price'].dtype)
print(" \n revenue for period in dataset : \n", chipo['item_price'].sum()) #KLOPT NIET
print(" \n how many orders were made : \n", chipo['order_id'].max())
#per order(diff entries), mean expenditure
print(" \n average revenue per order : \n", (chipo.groupby('order_id').sum())['item_price'].mean()) #KLOPT NIET
# amount of diff items sold : unique elements in item_name
print(" \n how many different items are sold : \n", chipo['item_name'].value_counts().count())
