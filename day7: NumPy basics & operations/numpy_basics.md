Numpy is a powerful python library used for:

- fast numerical computation
- working with arrays and matrices
- performing vectorized operations without loops
- it makes the operation speed closer to C/C++

## import numpy

```python
import numpy as np
```

## Array creation

```python
import numpy as np
a = np.array([1,2,3,4])
print(a)
```

- NumPy's array class is called **ndarray**
- Attributes of an ndarray object are:

  - ndarray.ndim: number of dimensions of the array
  - ndarray.shape: dimension of the array
  - ndarray.size: total number of elements of the array
  - ndarray.dtype: an object describing type of elements in the array
  - ndarray.itemsize: size in bytes of each element of the array
  - ndarray.data: the buffer containing actual element of the array

  ```python
  import numpy as np
  a = np.arange(15).reshape(3,5)
  print(a)
  print(a.shape)
  print(a.dtype)
  print(a.dtype.name)
  print(a.itemsize)
  print(a.size)
  print(type(a))
  print(a.data)
  print(a.ndim)
  print(a.flatten())
  ```

```python
import numpy as np
a = np.array([1, 2, 3, 4])
b = np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]
c = np.linspace(0, 1, 5)  # [0. , 0.25, 0.5 , 0.75, 1. ]
z = np.zeros((2,3))  # 2x3 array filled with 0s
o = np.ones((3,2))   # 3x2 array filled with 1s
i = np.eye(3)  # 3x3 identity matrix
e = np.empty((2,3)) # 2x3 with initail content is random and depends on state of memory
```

## Indexing and Slicing

accessing a part of an array

For 1D array:

```python
arr = np.array([10,20,30,40,50])
print(arr[0])     # 10
print(arr[1:4])   # [20 30 40]
```

For 2D array:

```python
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[1,2])     # 6 (2nd row, 3rd column)
print(a[:,1])     # all rows, 2nd column → [2 5 8]
print(a[0:2, 1:3]) # subarray [[2,3],[5,6]]
```

## Operations

```python
import numpy as np

a = np.array([2,4,5,6,1])
b = np.arange(4)

c = b - a # [-2 -3 -3 -3  3]
print(c) # [ 0  1  4  9 16]
print(b**2) # [ 9.09297427 -7.56802495 -9.58924275 -2.79415498  8.41470985]
print(10*np.sin(a)) # [ True  True False False  True]
print(a<5) # [1 2 3 4 5]
b=b+1
print(b) # [ 2  8 15 24  5]
print(a*b) # element wise product, [ 2  8 15 24  5]
print(a@b) # matrix product, 54
print(a.dot(b)) # another matrix product, 54
print(b.sum(axis=0)) # 15
```

## Random

```python
import numpy as np
# Random float numbers between 0 and 1
np.random.rand(2,3)

# Random integers
np.random.randint(10, 50, size=(2,3))

# Random numbers from normal (Gaussian) distribution
np.random.normal(0, 1, (2,3))

# Simulate rolling a dice 10 times
dice = np.random.randint(1,7,10)
print(dice)

```

## Aggregate Functions

```python
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr.sum())      # 21
print(arr.min())      # 1
print(arr.max())      # 6
print(arr.mean())     # 3.5
print(arr.std())      # 1.707...
print(arr.sum(axis=0))# [5 7 9] (column-wise)
print(arr.sum(axis=1))# [6 15]  (row-wise)

```
