## Function declaration

def functionName(parameter1, parameter2):
	# statement
	return expression
```python
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)
```

## Type of Arguments
1. Default arguments
2. Keyword arguments
3. Positional arguments
4. Arbitrary arguments

## Lambda Function
+ it is a anonymous (nameless) function that you can define in single line using lambda keyword
+ lambda argument: expression
```python
# normal function
def square(x):
    return x * x

# lambda function
square_lambda = lambda x: x * x

add = lambda a, b: a + b

print(add(10, 20))  # 30
print(square(5))         # 25
print(square_lambda(5))  # 25

```
