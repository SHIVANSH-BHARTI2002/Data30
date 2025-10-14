# Matplotlib

+ matplotlib is a python library for data visualization
+ Developed by John D. Hunter in 2003

## Importing 

```python
import matplotlib.pyplot as plt
```

- `matplotlib` is the main package
- `pyplot` is a sub-module that provides a simple interface similar to MATLAB

## Basic Plots in Matplotlib

### 1. Line plot
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis (Time)")
plt.ylabel("Y-axis (Value)")
plt.show()

```

- `plt.plot(x, y)` → plots a line joining the points (x[i], y[i])
- `plt.title()` → adds a title
- `plt.xlabel()`, `plt.ylabel()` → label the axes
- `plt.show()` → displays the plot

### 2. Bar plot
```python
categories = ['A', 'B', 'C', 'D']
values = [10, 25, 15, 30]

plt.bar(categories, values, color='orange')
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

```

- `plt.bar()` → creates vertical bars
- You can add color, width, or even horizontal bars with `plt.barh()`

### 3. Scatter plot

```python
x = [5, 7, 8, 10, 12]
y = [12, 14, 17, 20, 22]

plt.scatter(x, y, color='green', marker='o')
plt.title("Scatter Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
```

- Each point (x, y) is drawn as a dot
- Good for showing **positive or negative correlation**

### 4. Histogram
```python
import numpy as np

data = np.random.randn(1000)  # Generate 1000 random numbers

plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

- `plt.hist()` groups data into “bins” and shows frequency
- Great for understanding data distribution (e.g., normal, skewed)

## Plot Customization
### Titles and Labels
```python
plt.title("Monthly Sales Data", fontsize=14, color='blue')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales", fontsize=12)
```

### Line style and colors
You can modify line color, style, and markers:

```python
plt.plot(x, y, color='red', linestyle='--', marker='o')
```

Common options:
- `color`: `'red'`, `'blue'`, `'green'`, `'#ff5733'`
- `linestyle`: `'-'` (solid), `'--'` (dashed), `'-.'`, `':'`
- `marker`: `'o'`, `'^'`, `'s'` (circle, triangle, square)

### Adding legend
```python
plt.plot(x, y, label='Product A')
plt.plot(x, [i*1.5 for i in y], label='Product B')

plt.legend()
plt.title("Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
```

### Grid and axis limits
```python
plt.grid(True)
plt.xlim(0, 10)
plt.ylim(0, 50)
```

## Multiple plots using subplot()

+ You can show multiple graphs in one window using `plt.subplot()`
```python
plt.subplot(rows, columns, plot_number)
```

**Example:**
```python
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(1, 2, 1)   # 1 row, 2 columns, 1st plot
plt.plot(x, y1, color='blue')
plt.title("Sine Wave")

plt.subplot(1, 2, 2)   # 1 row, 2 columns, 2nd plot
plt.plot(x, y2, color='red')
plt.title("Cosine Wave")

plt.show()
```

- `plt.subplot(1, 2, 1)` → divides the window into 1 row and 2 columns, selects the first subplot
- Useful for **side-by-side comparison**
