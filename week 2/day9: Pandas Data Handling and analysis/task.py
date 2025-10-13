# Clean a dataset with missing values and 
# group it by a specific column to find the average of another column.

import pandas as pd

df = pd.read_csv('student.csv')
print("----------MISSING VALUES----------")
print(df)
print('\n')

print("----------CLEAN DATA SET----------")
clean_df = df.dropna()
print(clean_df)
print('\n')

print("----------GROUPING BY CLASS & AVERAGE OF MARKS----------")
grouped = df.groupby('Class')['Maths'].mean()
print(grouped)

