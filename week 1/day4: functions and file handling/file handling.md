## Access modes

1. read only 'r'
2. read and write 'r+'
3. write only 'w'
4. write and read 'w+'
5. append only 'a'
6. append and read 'a+'

## Create a file in python

- open() function with following options- 'x' or 'w'
- "x": it will create new file if and only if no file already exist with that name, else return error

```python
f = open("test.txt", "x")
```

- "w": this command will create a new text file, it will not return an error if file exist, it will over write it

```python
f = open("test.txt", "w")
```

## Write to a File

### write( ) method:

- this will inserts the string into the text file on a single line

```python
f.write("hello world!")
```

### writelines( ) method:

- to insert multiple lines

```python
f.writelines(["hello world,", "whats up!"])
```

## Read from Text File

### read( ) method:

- This function returns the bytes read as a string. If no n is specified, it then reads the entire file

```python
f = open("test.txt", "r")
print(f.read())
```

### readline( ) method:

- this method read lines from a file and return it as a string
- It reads at most n bytes for the specified n
- But even if n is greater than the length of the line, it does not read more than one line

```python
f = open("text.txt", "r")
print(f.readline())
```

### readlines( ) method:

- This function reads all of the lines and returns them as string elements in a list, one for each line
- You can read the first two lines by calling `readline()` twice, reading the first two lines of the file

```python
f = open("test.txt", "r")
print(f.readline())
print(f.readline())
```

## Close a Opened file

### close( ) method

```python
f = open("myfiles.txt", "r")
print(f.readline())
f.close()
```
