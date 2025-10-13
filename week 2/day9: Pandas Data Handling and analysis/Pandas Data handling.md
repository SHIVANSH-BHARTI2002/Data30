# Pandas Data Handling And Analysis

# Handling Missing Data

- real world datasets often contains missing values (NaN)
- Pandas provides functions to detect, remove, or fill them
- Example DataFrame with missing values:

```python
import pandas as pd
import numpy as np

data = {
    'Name': ['Aman', 'Priya', 'Shivansh', 'Neha', 'Raj'],
    'Maths': [85, np.nan, 75, 89, 60],
    'Physics': [78, 88, np.nan, 92, 65],
    'Chemistry': [82, 85, 78, np.nan, 70]
}

df = pd.DataFrame(data)
print(df)
```

### Detect missing values: isnull()

```python
print(df.isnull())
```

- return True where data is missing
- To count missing values per column:

```python
print(df.isnull().sum())
```

### Drop missing values: dropna()

- remove rows (or column) with missing values

```python
df_clean = df.dropna()
print(df_clean)
```

- to drop column instead:

```python
df.dropna(axis=1)
```

### Fill Missing Values: fillna()

- Replace missing values with specific values or strategy

```python
df['Maths'].fillna(df['Maths'].mean(), inplace=True)
df['Physics'].fillna(0, inplace=True)
df['Chemistry'].fillna(df['Chemistry'].median(), inplace=True)
print(df)
```

## Data Filtering: Conditional Selection

- you can fill row based on conditions using boolean indexing

```python
# Students scoring more than 80 in Maths
print(df[df['Maths'] > 80])

# Multiple conditions using & (AND), | (OR)
print(df[(df['Maths'] > 80) & (df['Physics'] > 80)])
```

## Sorting and Ranking

### Sorting Data: sort_values()

- you can sort data by any column(s)

```python
# Sort by Maths marks
print(df.sort_values(by='Maths'))

# Sort by multiple columns
print(df.sort_values(by=['Maths', 'Physics'], ascending=[False, True]))
```

### Ranking Data: rank()

- Assigns a rank number to each value in a column
- Ties get the same rank

```python
df['Maths_Rank'] = df['Maths'].rank(ascending=False)
print(df[['Name', 'Maths', 'Maths_Rank']])
```

## String Functions

- when you have text data, pandas allows applying string operations easily using .str

```python
names = pd.Series(['  shivansh  ', 'AMAN', 'Priya kumari', 'Neha', 'raj'])

# Convert to lowercase
print(names.str.lower())

# Remove spaces
print(names.str.strip())

# Extract substring
print(names.str[:5])

# Find length
print(names.str.len())

# Check if contains substring
print(names.str.contains('a'))
```

## Data Transformation

These methods help apply custom functions to transform data

### apply()

- Used to apply a function to each column or row

```python
def grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    else:
        return 'C'

df['Grade'] = df['Maths'].apply(grade)
print(df[['Name', 'Maths', 'Grade']])
```

### map()

- Used for serial only, applies a function or mapping to each elements

```python
df['Gender'] = ['M', 'F', 'M', 'F', 'M']
df['Gender'] = df['Gender'].map({'M': 'Male', 'F': 'Female'})
print(df[['Name', 'Gender']])
```

### lambda with apply()

- inline functions for quick transformation

```python
# Increase marks by 5%
df['Maths'] = df['Maths'].apply(lambda x: x * 1.05)
```

## Aggregation and Grouping

### Grouping data: groupby()

- group data by one or more columns, then applies an aggregation function (like mean, sum, or count)

```python
#sample data set

data = {
    'Class': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Name': ['Aman', 'Priya', 'Shivansh', 'Neha', 'Raj', 'Kriti'],
    'Maths': [85, 92, 75, 89, 60, 95],
    'Physics': [78, 88, 80, 92, 65, 90]
}
df = pd.DataFrame(data)
```

### Basic Grouping

```python
grouped = df.groupby('Class')
print(grouped.mean())
```

### Multiple Aggregations

```python
result = df.groupby('Class').agg({
    'Maths': ['mean', 'max', 'min'],
    'Physics': 'sum'
})
print(result)
```

### Counting Records per Group

```python
print(df.groupby('Class')['Name'].count())
```

### Reset Index After Grouping

```python
df_grouped = df.groupby('Class', as_index=False).mean()
print(df_grouped)
```
