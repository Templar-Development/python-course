# Lesson-2 | Building on Basics

## 1. More Advanced Data Structures

### Lists

Lists are ordered, mutable collections that can contain various data types.

Example:

```python
# List creation
fruits = ['apple', 'banana', 'orange']
```

### Dictionaries

Dictionaries are unordered collections of key-value pairs.

Example:

```python
# Dictionary creation
person = {'name': 'John', 'age': 30, 'city': 'New York'}
```

### Tuples

Tuples are ordered, immutable collections.

Example:

```python
# Tuple creation
coordinates = (3, 5)
```

### Sets

Sets are unordered collections of unique elements.

Example:

```python
# Set creation
unique_numbers = {1, 2, 3, 4, 5}
```

### Common Operations on Data Structures

Manipulate data structures using various methods (e.g., `append`, `remove`, `keys`, `values`).

Example:

```python
# Common operations on lists
fruits.append('grape')
fruits.remove('banana')
```

## 2. Loops

### `for` Loops

`for` loops are used for iterating over a sequence (like a list, tuple, or string) or other iterable objects.

Example:

```python
# For loop
for i in range(5):
    print(i)

# Output: 0 1 2 3 4
```

### `while` Loops

`while` loops continue executing as long as a certain condition is true.

Example:

```python
# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Output: 0 1 2 3 4
# Count is now 5
# Note: count += 1 is the same as count = count + 1
```

### Loop Control Statements

- `break`: Exits the loop prematurely.
- `continue`: Skips the rest of the code inside the loop for the current iteration.

Example:

```python
# Loop control statements
for i in range(10):
    if i == 3:
        break
    print(i)

# Output: 0 1 2
```

### Nested Loops

You can use loops inside other loops.

Example:

```python
# Nested loops
for i in range(3):
    for j in range(3):
        print(i, j)
```

## 3. Working with Files

### Reading from and Writing to Files

Use `open()` to interact with files. Modes include 'r' for reading, 'w' for writing, and 'a' for appending.

Example:

```python
# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()

# Writing to a file
with open('output.txt', 'w') as file:
    file.write('Hello, World!')
```

### Using `with` Statement for File Handling

The `with` statement ensures proper file handling by automatically closing the file when done.

Example:

```python
# File handling with 'with' statement
with open('example.txt', 'r') as file:
    content = file.read()
    # Process content here
# File is automatically closed outside the 'with' block
```

## 4. Working with Libraries

### Importing Libraries/Modules

Use `import` to bring functionality from external libraries into your code.

Example:

```python
# Importing a library/module
import math
result = math.sqrt(25)
```

### Exploring the Python Standard Library

Python's Standard Library offers a wide range of modules for various tasks.

Example:

```python
# Using the random module
import random
random_number = random.randint(1, 10)
```

### Basic Usage of External Libraries

Explore and utilize external libraries for specific tasks.

Example:

```python
# Using the requests library for HTTP requests
import requests
response = requests.get('https://www.example.com')
```

## Project: Hangman Game

In this project, you will implement a simple text-based Hangman game. This will allow you to practice using loops, working with lists and strings, and applying conditional statements.

### Requirements:

1. Choose a random word from a predefined list.
2. Display the initial state of the word with underscores for unknown letters.
3. Allow the user to guess a letter.
4. Update the display to show correctly guessed letters and track incorrect guesses.
5. Implement logic to determine if the user has won or lost.

### Bonus:

- Add a limit to the number of incorrect guesses allowed.
- Create a more extensive word list or implement a way to fetch words from an external source.
- Improve the user interface by displaying the hangman figure as incorrect guesses accumulate.

**Tip:** You can use the `random` module to generate a random number or choose a random item from a list.
