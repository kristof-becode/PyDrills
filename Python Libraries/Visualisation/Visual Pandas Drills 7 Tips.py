import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")

tips = pd.read_table('/home/becode/data/pandas/tips.csv', sep =',')
print(tips)

# Delete the Unnamed 0 column
tips = tips.drop(columns='Unnamed: 0')
print(tips)
"""
# Plot the total_bill column histogram
totBill = tips.total_bill
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.title('Total Bill')
#plt.hist(totBill, bins= 25, rwidth =0.95) # I will sue the Seaborn distplot below but this is the matplotlib hist
ax = sns.distplot(totBill, hist=True, color='blue')
plt.show()

# Create a scatter plot presenting the relationship between total_bill and tip
#sns.lmplot(x='total_bill', y='tip',data=tips, fit_reg=False,hue='Stage') # this is a scatterplot in seaborn but I need a jointplot
sns.jointplot(x='total_bill', y='tip',data=tips)
plt.ylim(0, 12)
plt.xlim(0, 60)
plt.show()

# Create one image with the relationship of total_bill, tip and size. Hint: It is just one function
sns.pairplot(tips)
plt.show()

# Present the relationship between days and total_bill value
sns.lmplot(x='day', y='total_bill',data=tips, fit_reg=False, hue='day', legend=False) # I don't need to see Hue legend, they are just the days
plt.show()

#  Create a scatter plot with the day as the y-axis and tip as the x-axis, differ the dots by sex
#sns.lmplot(x='tip', y='day',data=tips, fit_reg=False)#, hue='sex', legend=False) # I don't need to see Hue legend, they are just the days
sns.lmplot(x="tip", y="day", data=tips, fit_reg=False, hue="sex")
#sns.catplot(x="tip", y="day", hue="time",
                #height=3.5, aspect=1.5,
                #kind="box", legend=False, data=tips)
#plt.show()

# Create a box plot presenting the total_bill per day differentiation the time (Dinner or Lunch)
sns.catplot(x="day", y="total_bill", hue="time", height=3.5, aspect=1.5, kind="box", legend=True, data=tips)
plt.show()

# Create two histograms of the tip value based for Dinner and Lunch. They must be side by side.
tipsLunch = tips.tip[tips.time == 'Lunch']
tipsDinner = tips.tip[tips.time == 'Dinner']
plt.subplots(1, 2, sharey=True) # He doesn't sharey...why?
plt.subplot(121)
plt.hist(tipsLunch, bins = 10, color='blue')
plt.title("Tips @Lunch")
#sns.distplot(tipsLunch, hist=True, color='blue')
plt.subplot(122)
plt.hist(tipsDinner, bins = 10, color='blue')
plt.title("Tips @Dinner")
#sns.distplot(tipsDinner, hist=True, color='blue')
plt.show()
"""
# Create two scatterplots graphs, one for Male and another for Female, presenting the total_bill value and tip relationship, differing by smoker or no smoker¶
# They must be side by side

sns.lmplot(x="total_bill", y="tip", col="sex", hue='smoker', fit_reg=False, data=tips)
plt.ylim(0, 12)
plt.xlim(0, 60)
plt.show()