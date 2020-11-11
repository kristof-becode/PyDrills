import numpy as np
import pandas as pd

chipo = pd.read_table('/home/becode/data/pandas/chipotle.tsv')

# DO NOT FORGET TO MAKE ITEM_PRICE FLOAT64 AS IN EXERCISE 1 !!!!!
chipo['item_price'] = chipo['item_price'].apply(lambda str : str[1:])
chipo['item_price'] = chipo['item_price'].astype('float64')
# END OF MESSAGE

print(chipo.sort_values(by = 'quantity').head(30))
#chipo = chipo.drop_duplicates(subset=['quantity', 'item_name'], keep = 'first')
#chipo = chipo.drop_duplicates(subset= [ 'item_name'], keep = ['quantity'] == 1)
#chipo = chipo.drop_duplicates()
print(chipo.sort_values('item_name'))

newchipo = chipo[['item_name' , 'item_price']] # new dataframe
print(newchipo)
#print(chipo[['item_name' , 'item_price']].head(30))
print(chipo.sort_values('item_name').head(30))
print(chipo.item_price.max())
#print(chipo.item_price.max()['quantity'])
print(chipo.quantity[chipo.item_price == chipo.item_price.max()]) # ['quantity'])
#print(chipo['quantity'])
print(chipo.item_name[chipo.item_name == 'Veggie Salad Bowl'].count())
print(chipo.quantity[(chipo.quantity > 1) & (chipo.item_name == 'Canned Soda')].count())