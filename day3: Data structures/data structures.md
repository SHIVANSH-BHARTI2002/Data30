## Build-in Data Structures

### 1. List

- ordered
- mutable
- items in a list do not need to be of the same type
- represented using [ ]
- \*\*example:

```
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add element
print(fruits[0])         # Access first element

```

### 2. Tuple

- ordered
- immutable
- faster than list
- represented using ( )
- **example: **

```
point = (2, 3)
print(point[1])  # Access second element

```

### 3. Set

- unordered
- mutable
- does not allow duplicate values
- insertion, deletion, traversal takes O(1) on average
- If Multiple values are present at the same index position, then the value is appended to that index position, to form a Linked List
- represented using { }
- support operations like union, intersection

```
numbers = {1, 2, 3, 2}
numbers.add(4)
print(numbers)  # {1, 2, 3, 4}

```

### 4. Dictionary

- collection of key value pairs
- unordered
- key must be unique
- representation using { ( ) }
- **Example:**

```
student = {"name": "Rohit", "age": 22}
print(student["name"])  # Rohit
student["age"] = 23

```

### 5. Strings

- any thing written under ' ' or " "
- immutable
- no character datatype, its only string with length of 1
- **Example:**

```
name = "Python"
print(name[0])   # 'P'
print(name.upper())  # 'PYTHON'
```
