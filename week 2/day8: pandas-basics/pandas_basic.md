# Basics

- short for Python Data Analysis Libraries is a powerful, open-source library used for data manipulation, analysis, and cleaning in python
- it provide high-performance, easy-to-use data structures, and tools for working with structured(tabular) data
- support multiple file formats like: CSV, Excels, JSON, SQL, HTML

# import pandas

```python
import pandas as pd
```

# Data structures in Pandas

Pandas provide two types of data-structures:

- Series
- DataFrame

## Series (1-Dimensional)

- A series is one-dimensional labeled array, similar to a single column in excel or a list with indexes

```python
import pandas as pd

data = [10,20,30,40]
s = pd.Series(data)
print(s)
```

### custom index

```python
import pandas as np
s = pd.Series([10,20,30],index=['a','b','c'])
print(s)
```

## DataFrame (2-Dimensional)

- A DataFrame is a two-dimensional labeled data structure like an excel sheet or SQL table

```python
import pandas as pd
data = {'Name' : ['cris','rohan','aman'],
		'Age' : [20,21,19],
		'Marks' : [55,43,23]}
df = pd.DataFrame(data)
print(df)
```

## Creating DataFrame

1. From list

```python
data = [['Aman', 21], ['Priya', 19], ['Shivansh', 20]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
```

2. From Dictionary

```python
data = {'Name': ['Aman', 'Priya', 'Shivansh'],
        'Age': [21, 19, 20]}
df = pd.DataFrame(data)

```

3. From numpy array

```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df)

```

4. From CSV file

```python
df = pd.read_csv('data.csv')
```

## Reading and Writing Data

### Reading Data

- read_csv()
  - reading from CSV file

```python
df = pd.read_csv('data.csv')
```

- read_excel()
  - reading from excel file

```python
df = pd.read_excel('data.xlsx')
```

- read\_\_json()
  - reading JSON data

```python
df = pd.read_json('data.json')
```

### Writing Data

- to_csv()

```python
df.to_csv('output.csv')
```

- to_excel()

```python
df.to_excel('output.xlsx',index = False)
```

- to_json()

```python
df.to_json('output.json')
```

## Inspecting Data

- Once a DataFrame is created or read, you can **inspect** it using these methods
- df.head(n): shows the first n rows (default 5)
- df.tail(n): shows the last n rows (default 5)
- df.info(): summary of columns, data types, non-null counts
- df.describe(): descriptive statistics (mean, std, min, max, etc.)
- df.shape: returns tuples (rows, columns)
- df.columns: return all columns names

```python
print(df.head())       # Top 5 rows
print(df.tail(2))      # Last 2 rows
print(df.info())       # Column summary
print(df.describe())   # Numerical summary
print(df.shape)        # (rows, columns)
```

## Selecting Data

There are two main accessors in Pandas for selecting data:

- loc[]: Label-based indexing
- iloc[]: integer-based indexing

### Using loc[]

- use row and column labels

```python
df = pd.DataFrame({
    'Name': ['Aman', 'Priya', 'Shivansh'],
    'Age': [21, 19, 20],
    'Marks': [88, 92, 79]
}, index=['s1', 's2', 's3'])

# Select single row
print(df.loc['s1'])

# Select specific rows and columns
print(df.loc[['s1', 's3'], ['Name', 'Marks']])
```

### Using iloc[]

- use numerical indexes like in numpy arrays

```python
# Select 1st row
print(df.iloc[0])

# Select first 2 rows and first 2 columns
print(df.iloc[0:2, 0:2])

```

### Boolean Filtering

- Filter rows based on conditions

```python
# Select students with Marks > 80
print(df[df['Marks'] > 80])
```
