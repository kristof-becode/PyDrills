import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")

online_rt = pd.read_table('/home/becode/data/pandas/Online_Retail.csv', encoding = 'latin1', sep =',')
print(online_rt)

# Create a histogram with the 10 countries that have the most 'Quantity' ordered except UK # THIS IS A PLOT BAR
sns.distplot(x,y)
plt.title('Histogram')
