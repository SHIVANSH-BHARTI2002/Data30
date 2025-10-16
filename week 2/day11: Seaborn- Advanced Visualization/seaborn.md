# Seaborn

- Seaborn is a python data visualization library built on top of matplotlib
- It provides a high-level interface for creating attractive and informative statistical graphics

# Import seaborn

```python
import seaborn as sns
import matplotlib as plt
```

# Dataset Functions in Seaborn

Seaborn comes with built-in datasets for practice

## 1. sns.get_dataset_names()

Lists all available built-in datasets

```python
import seaborn as sns

print(sns.get_dataset_names())
```

## 2. sns.load_dataset(name)

loads a dataset as a panda dataframe

```python
df = sns.load_dataset("trips")
print(df.head())
```

# Common Seaborn Plots

## 1. barplot()- Mean of a numerical variable

Shows **average value** (with confidence interval bars) of one variable grouped by another

```python
sns.barplot(x="day", y="total_bill", data=df)
plt.show()
```

- Default behavior: plots **mean** of `total_bill` per `day`.
- You can change estimator (e.g., median):

```python
import numpy as np
sns.barplot(x="day", y="total_bill", data=df, estimator=np.median)
plt.show()

```

## 2. countplot()- Frequency of categories

plots the count of each category

```python
sns.countplot(x="day", data=df)
plt.show()
```

Equivalent to,

```python
df['day'].value_counts().plot(kind='bar')
```

## 3. boxplot()- Summary of data distribution

Shows **median, quartiles, outliers**

```python
sns.boxplot(x="day", y="total_bill", data=df)
plt.show()
```

**Interpretation:**

- Box = Interquartile range (IQR)
- Line inside box = Median
- Whiskers = Range of data
- Dots = Outliers

## 4. violinplot()- Distribution + Density

A **combination of boxplot + KDE (Kernel Density Estimation)**

```python
sns.violinplot(x="day", y="total_bill", data=df)
plt.show()
```

- Great for visualizing **distribution symmetry and density**.
- You can combine with `hue` for comparisons:

```python
sns.violinplot(x="day", y="total_bill", hue="sex", data=df, split=True)
plt.show()
```

## 5. pairplot()- Pairswise relationships between features

Used to visualize **relationships among all numeric columns**

```python
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")
plt.show()
```

Diagonal → histograms of each feature

- Off-diagonal → scatter plots between features
- `hue` → color grouping

# Styling with seaborn

## 1. Themes– Control background & grid style

use:

```python
sns.set_style("whitegrid")  # Options: darkgrid, whitegrid, dark, white, ticks
```

Example:

```python
sns.set_style("darkgrid")
sns.boxplot(x="day", y="tip", data=df)
plt.show()
```

## 2. Color palettes

Change colors easily

```python
sns.set_palette("pastel")
sns.barplot(x="day", y="total_bill", data=df)
plt.show()
```

common palettes:

- deep
- muted
- pastel
- bright
- dark
- colorblind
  or custom palettes, example:

```python
sns.set_palette(["#FF9999", "#66B2FF", "#99FF99", "#FFCC99"])
```

# Integration with Pandas

- Seaborn is built to work directly with pandas dataframes
- You can directly pass:
  - `data=df`
  - and refer to columns by name.

```python
import pandas as pd

# Create your own DataFrame
data = pd.DataFrame({
    "Category": ["A", "B", "A", "C", "B", "C"],
    "Value": [10, 20, 15, 25, 22, 30]
})

sns.barplot(x="Category", y="Value", data=data)
plt.show()

```

# Seaborn vs Matplotlib

| Feature             | Seaborn                          | Matplotlib                |
| ------------------- | -------------------------------- | ------------------------- |
| syntax              | high level                       | low level                 |
| Aesthetics          | automatically styled             | manual                    |
| Pandas support      | directly integrated              | must extract columns      |
| Statistical support | built-in                         | manual implementation     |
| Default Colors      | beautiful palettes               | basic colors              |
| Purpose             | quick, clean, statistical visual | full control, but verbose |
