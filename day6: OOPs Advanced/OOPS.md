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

## Inheritance

- child class use attributes/methods of parent class
- Types
  - **Single**
  ```python
  class Parent:
  	def func1(self):
  		print("Parent class")
  class Child(Parent):
  def func2(self):
  	print("child class")
  ob1 = Child()
  ob1.func1()
  ob1.func2()
  ```
  - **Multiple**
  ```python

  ```

# Base class 1

class Mother:
mothername = ""

    def mother(self):
        print(self.mothername)

# Base class 2

class Father:
fathername = ""

    def father(self):
        print(self.fathername)

# Derived class

class Son(Mother, Father):
def parents(self):
print("Father :", self.fathername)
print("Mother :", self.mothername)

# Driver code

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()
`
	+ **Multilevel**
	`python # Base class
class Grandfather:
def **init**(self, grandfathername):
self.grandfathername = grandfathername

# Intermediate class

class Father(Grandfather):
def **init**(self, fathername, grandfathername):
self.fathername = fathername # Call the constructor of Grandfather
Grandfather.**init**(self, grandfathername)

# Derived class

class Son(Father):
def **init**(self, sonname, fathername, grandfathername):
self.sonname = sonname # Call the constructor of Father
Father.**init**(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

# Driver code

s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()
`
	+ **Hierarchical**
	`python # Base class
class Parent:
def func1(self):
print("This function is in parent class.")

# Derived class 1

class Child1(Parent):
def func2(self):
print("This function is in child 1.")

# Derived class 2

class Child2(Parent):
def func3(self):
print("This function is in child 2.")

# Driver code

object1 = Child1()
object2 = Child2()

object1.func1()
object1.func2()
object2.func1()
object2.func3()
`
	+ **Hybrid**
	`python # Base class
class School:
def func1(self):
print("This function is in school.")

# Derived class 1 (Single Inheritance)

class Student1(School):
def func2(self):
print("This function is in student 1.")

# Derived class 2 (Another Single Inheritance)

class Student2(School):
def func3(self):
print("This function is in student 2.")

# Derived class 3 (Multiple Inheritance)

class Student3(Student1, School):
def func4(self):
print("This function is in student 3.")

# Driver code

obj = Student3()
obj.func1()
obj.func2()
```

## Method overriding

- child class redefines parent method

```python
class Animal:
    def sound(self): print("Generic sound")
class Dog(Animal):
    def sound(self): print("Bark")

```

- using super( ): use to give access to methods and properties of parent or sibling class

```python
class Dog(Animal):
    def sound(self):
        super().sound()   # Calls parent method
        print("Bark")

```

## Polymorphism

- Duck Typing

```python
class Dog:
    def speak(self): print("Bark")
class Cat:
    def speak(self): print("Meow")

def make_sound(animal):
    animal.speak()

make_sound(Dog())   # Bark
make_sound(Cat())   # Meow

```

- Operator overloading
- overloading addition operator

```python
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

Ob1 = Complex(1, 2)
Ob2 = Complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)

```

- overloading comparison operator

```python
class A:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        return self.a > other.a

ob1 = A(2)
ob2 = A(3)
if ob1 > ob2:
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")
```

## Abstraction

- Abstract base class are created using abc module and @abstractmethod decorator

```python
from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())
```

- **Abstract Properties:** work like abstract methods but are used for properties, these properties are declared with @property decorator and marked as abstract using @abstractmethod. Sub classes must implement these properties

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass  # Abstract property, must be implemented by subclasses

class Dog(Animal):
    @property
    def species(self):
        return "Canine"

# Instantiate the concrete subclass
dog = Dog()
print(dog.species)
```
