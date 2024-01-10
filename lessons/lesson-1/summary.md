# Lesson-1 | Intro to Python

## 1. Basics of Python/Coding

### Introduction to Python

Python is a high-level, interpreted programming language known for its readability and simplicity. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

### Python Syntax

Python syntax is straightforward and easy to understand. Indentation is crucial for defining blocks of code, and colons (`:`) are used to signify the beginning of a new block.

Example:

```python
# Example of Python syntax
if True:
    print("This is a valid block")
else:
    print("This is also a valid block")
```

### Running Python Code

Python code can be executed in several ways, including using an interpreter, a script file, or an integrated development environment (IDE).

Example (running a Python script):

```bash
python script.py
```

## 2. Variables

### Understanding Variables

Variables are containers for storing data values. In Python, you can assign various data types to variables, such as integers, floats, strings, etc.

Example:

```python
# Variable assignment
age = 25
name = "John"
```

### Variable Naming Conventions

Follow PEP 8 conventions for variable names. Use lowercase with underscores for readability.

Example:

```python
# Variable naming
user_age = 30
```

### Assigning Values to Variables

You can assign values to variables using the assignment operator (`=`).

Example:

```python
# Assigning values to variables
x = 10
y = 5
```

## 3. Conditionals

### If Statements

Conditional statements, like `if`, allow you to make decisions in your code based on certain conditions.

Example:

```python
# If statement
if x > y:
    print("x is greater than y")
```

### Else and Elif Statements

`else` and `elif` (else if) statements extend the decision-making capability by providing alternative paths.

Example:

```python
# Else and Elif statements
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")
```

### Logical Operators

Logical operators (e.g., `and`, `or`, `not`) are used to combine conditional statements.

Example:

```python
# Logical operators
if x > 0 and y > 0:
    print("Both x and y are positive")
```

## 4. Functions

### Defining Functions

Functions are blocks of reusable code. Define them using the `def` keyword.

Example:

```python
# Function definition
def greet(name):
    return f"Hello, {name}!"
```

### Function Parameters and Return Values

Functions can take parameters as input and return values as output.

Example:

```python
# Function with parameters and return value
def add(x, y):
    return x + y
```

### Scope and Lifetime of Variables

Variables have scope, defining where they can be accessed, and a lifetime, indicating how long they exist.

Example:

```python
# Scope and lifetime of variables
def example_function():
    local_variable = "I am local"
    print(local_variable)
```

## 5. User Input

### Using the `input()` Function

The `input()` function allows user interaction by taking input from the console.

Example:

```python
# Taking user input
user_name = input("Enter your name: ")
```

### Handling User Input

Handle user input by validating and processing it appropriately.

Example:

```python
# Handling user input
try:
    user_age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid age.")
```

### Type Conversion

Convert data types as needed, especially when dealing with user input.

Example:

```python
# Type conversion
user_height = float(input("Enter your height in meters: "))
```

## Project: Simple Calculator

In this project, you will create a simple calculator program that can perform basic arithmetic operations. The goal is to apply the concepts learned in this lesson to build a functional and interactive Python program.

### Requirements:

1. Implement functions for addition, subtraction, multiplication, and division.
2. Take user input for two numbers and the desired operation.
3. Display the result of the chosen operation.

### Bonus:

- Add error handling to handle invalid input, such as non-numeric values.
- Expand the calculator to include additional mathematical operations (e.g., exponentiation, square root).
