import random

import numpy
import numpy as np
import pandas as pd

ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr_np = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # creating Numpy array
print(ar)
print(arr_np)

# Creating 2D array
Matrix_array = [[1,2,3], [4,5,6]]
matrix_array_np = numpy.array([[1,2,3], [4,5,6]])
print(Matrix_array)
print(matrix_array_np)

#Basic operation
print(np.sum(arr_np)) # sum of all elements in array
print(numpy.mean(arr_np)) # mean of array total number divided by how many numbers are there
print(numpy.transpose(matrix_array_np)) # transpose of the 2D matrix

# ************************************ Pandas *******************************************
data = [10, 20, 30, 40]
series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(series)

dataFrame = {
    'name': ['Jack', 'Jelly', 'Job', 'Charlie'],
    'age': [25, 21, 30, 31],
    'city': ['chennai', 'bangalore', 'coimbatore', 'chennai']
}
df = pd.DataFrame(dataFrame)
print(df)

# Reading the file
'''
df.to_csv('C:\desktop\data.csv', index=False)
df = pd.read_csv('data.csv')
'''
print(df['name']) # Select a coloumn
print(df.loc[1]) # Select a row by index
print(df.iloc[1, 1]) # Select specific cell

filter_df = df[df['age'] > 30]
print(filter_df)
print(len("mukesh"))

# Create pandas dataframe with datetime index and one column filled with random integers

date_rng = pd.date_range(start='2020-01-01', end='2025-12-31', freq='D')
df = pd.DataFrame(date_rng, columns=['date'])
df['data'] = np.random.randint(100, 300, size=(len(date_rng)))
df.set_index('date', inplace=True)
print("Original DataFrame:")
print(df)

monthly_mean = df.resample('M').mean()
print("Monthly mean DataFrame:")
print(monthly_mean)