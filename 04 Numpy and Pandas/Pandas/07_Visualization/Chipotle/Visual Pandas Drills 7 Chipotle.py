import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

chipo = pd.read_table('/home/becode/data/pandas/chipotle.tsv')
print(chipo.head(5))

# set item_price as float64, remove dollar sign
chipo['item_price'] = chipo['item_price'].apply(lambda str : str[1:])
chipo['item_price'] = chipo['item_price'].astype('float64')

#  Create a histogram of the top 5 items bought => THIS IS NO HISTOGRAM BUT A BAR CHART!!!!!!!!!!
NewFrame = pd.DataFrame(chipo.groupby('item_name')['quantity'].sum().reset_index()) # reset_index does the trick so I can work freely with these columns in the new dataframe
NewFrame = NewFrame.sort_values(by='quantity', ascending=False) #STRANGE TAHT I HAVE TO TELL HIM BY QUANTITY...
#print(NewFrame)
#print(NewFrame.quantity)
Names = NewFrame.item_name.iloc[:5] # select 5 item_names with most quantity
#print(Names)
Orders =  NewFrame.quantity.iloc[:5] #select respective 5 quantities
#print(Orders)
plt.bar(Names, Orders, width = 0.5) # PLOT BAR !!!
plt.xticks(rotation =90)
plt.title('Order quantities for most ordered items')
plt.show()
"""
#Create a scatterplot with the number of items orderered per order price¶
#Hint: Price should be in the X-axis and Items ordered in the Y-axis
orderPrice = pd.DataFrame(chipo.groupby('order_id').item_price.sum()) # Dataframe with Order Prices or sum item_prices per order
orderQuantity = pd.DataFrame(chipo.groupby('order_id').quantity.sum()) # Datframe - Quantities per order id
x = orderPrice.item_price
y = orderQuantity.quantity# chipo.groupby('item_price')['quantity'].sum()
plt.scatter(x,y, c='green', alpha=0.8, edgecolors='black')
plt.xlabel('price order')
plt.ylabel('# items ordered')
plt.title('items ordered per order price')
plt.axis([0,250,0,40])
plt.show()
"""