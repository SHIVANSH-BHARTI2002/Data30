import pandas as pd

df = pd.read_csv('students.csv')
print("---BASIC INFORMATION---")
print(df.info())
print("\n---TOP 5 ROWS---")
print(df.head())
print("\n---SUMMARY---")
print(df.describe())