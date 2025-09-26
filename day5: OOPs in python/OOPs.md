## Class and Object

creating class in python

```python
#Class creation
class Car:
	def __init__(self,brand,model):
		self.brand = brand
		self.model = model

#object creation
car1 = Car("Tesla", "Model S")

print(car1.brand, car2.model)

```

## \_\_init\_\_ method (Constructor)

- automatically called when new object is created

```python
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

s1 = Student("Shivansh", 101)
print(s1.name, s1.roll_no)  # Shivansh 101

```

## Methods

- python has 3 methods inside classes

#### Instance Methods

- Operates on individual objects
- have access to self (object itself)

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):  # Instance method
        print(f"{self.name} is barking!")

d = Dog("Bruno")
d.bark()   # Bruno is barking!

```

#### Class Methods

- work at the class level (not object level)
- use @classmethod decorator
- take cls (class itself) as first parameter

```python
class Employee:
    company = "Google"  # Class variable

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee()
print(Employee.company)  # Google
Employee.change_company("Microsoft")
print(Employee.company)  # Microsoft

```

#### Static Methods

- independent function inside a class
- do not use self or cls
- declared with @staticmethod

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))  # 8

```

## Encapsulation

- Public
  - accessible everywhere
  ```python
  self.name = "python"
  ```
- Private
  - indicated by double \_\_
  - cannot be access directly outside class
  ```python
  self.__salary = 50000
  ```
- Protected
  - indicated by a single underscore \_
  - scope within its class and sub class
  ```python
  self._age = 21
  ```
