import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")

apple = pd.read_table('/home/becode/data/pandas/appl_1980_2014.csv', sep =',')
print(apple.head(10))
print(apple.shape)

# Check out the type of the columns
print("\n Check out the type of the columns: \n",apple.dtypes)

# Transform the Date column as a datetime type #datetime64[ns]
apple.Date = pd.to_datetime(apple.Date)
print("\n Transform the Date column as a datetime type: \n",apple.Date.dtype)

#  Set the date as the index
apple = apple.set_index('Date')
print("\n Set the date as the index: \n", apple.head(10))

# Is there any duplicate dates?
print("\n Is there any duplicate dates?: \n", apple.duplicated == True)

# Oops...it seems the index is from the most recent date. Make the first entry the oldest date # JUST MEANS REVERS ORDER with sort_values
apple = apple.sort_values(by='Date', ascending=True)
print("\n Sort on date, ascending: \n", apple)

# Get the last business day of each month


# What is the difference in days between the first day and the oldest
print("\n end date :", apple.index.max())
print("start date :", apple.index.min())
diff = apple.index.max()-apple.index.min()
print("? difference in days :", diff)

# How many months in the data we have?  # THIS IS NOT SOLVED IN THE WAY IT OUGHT TO BE SOLVED!!!!!!
print("\n ? many months in the data we have: \n", round(diff/np.timedelta64(1,'M'),1))

# Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches
x = apple.index # If I use apple.Date I get an error so I have to point to index column instead(which is Date)!!
y = apple['Adj Close']
plt.figure(1, figsize=(13.5,9))
plt.plot(x,y)
plt.title('Adj close vs time')
plt.show()