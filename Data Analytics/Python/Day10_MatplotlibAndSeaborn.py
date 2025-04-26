import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

x=[0,2,4,6,8]
y=[1,3,5,10,9]
y1=[2,6,2,7,4]

#print(plt.plot(x,y))

plt.xlabel('Fruits')
plt.ylabel('Price')
plt.title('Basic line plot')
#print(type(x))

# creating customized graph
#plt.subplot(2,2,1)
#plt.plot(x,y1,color='green')
#plt.title("Plot 1")
#plt.subplot(x,y1,color='red')
#plt.grid()
#plt.show(True)


#plt.plot([0,5,4,10,8], [1,2,5,10,9], color='yellow', linestyle='--')
#plt.plot(x,y,)
#plt.show()

#******************** Bar plot ******************
#plt.bar(['Apple', 'Bannana', 'Carrot', 'Ornage', 'Mango'], [10, 5, 20, 27, 25], color='red', edgecolor='black')


#******************** Histogram plot ******************
''' 
data = [2,3,6,8,9]
plt.hist(data, bins=5)
plt.title("Histogram")
'''


#******************** Scatter plot ******************

#plt.scatter(x, y, color='red', marker='*')


#******************** Pie chart ******************

"""size = [10, 30, 45, 20, 65]
lables = ['Apple', 'Bannana', 'Carrot', 'Ornage', 'Mango']
colour = ['red', 'yellow', 'blue', 'orange', 'green']
explod = [0,1,0,0,1]
plt.pie(size, labels=lables, explode=explod, colors=colour, autopct='%1.2f%%', shadow=True)
"""

#***************** Seaborn ***********************

tips = sns.load_dataset('tips')

sns.lineplot(data=tips, x='total_bill', y='tip')
plt.title("line plot of total bill vs tip")
plt.show()

sns.scatterplot(data=tips, x='total_bill', y='tip', markers='o', color='red')

sns.violinplot(data=tips, x='day', y='tip', color='yellow')

