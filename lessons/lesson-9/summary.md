# Lesson-9 | Python Advanced Concepts

## 1. Decorators

### Understanding Decorators and Their Use Cases

Decorators are a powerful feature in Python, allowing the modification of functions or methods. They are often used for tasks such as logging, memoization, or access control.

### Creating and Applying Decorators

Define decorators as functions and apply them to other functions.

Example:

```python
# Creating and applying decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```

### Decorators with Arguments

Enhance decorators by allowing them to take arguments.

Example:

```python
# Decorators with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()

# Output:
# Hello!
# Hello!
# Hello!
```

## 2. Generators

### Introduction to Generators

Generators are a memory-efficient way to iterate over large datasets. They produce values one at a time using the `yield` statement.

### Using the `yield` Statement

Use `yield` to create a generator function.

Example:

```python
# Using the yield statement in generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)

# Output:
# 5
# 4
# 3
# 2
# 1
```

### Generator Expressions

Create concise generators using generator expressions.

Example:

```python
# Generator expressions
squares = (x**2 for x in range(5))
for square in squares:
    print(square)

# Output:
# 0
# 1
# 4
# 9
# 16
```

## 3. Concurrency Basics (Threads and/or Multiprocessing)

### Overview of Concurrency

Concurrency is the execution of multiple tasks simultaneously.

### Threading in Python

Use the `threading` module to introduce parallelism.

Example:

```python
# Threading in Python
import threading

def print_numbers():
    for i in range(5):
        print(i)

def print_letters():
    for letter in 'ABCDE':
        print(letter)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

# Output:
# 0
# A
# 1
# B
# 2
# C
# 3
#...
```

### Multiprocessing in Python

Use the `multiprocessing` module to achieve parallelism.

Example:

```python
# Multiprocessing in Python
import multiprocessing

def square(x):
    return x**2

with multiprocessing.Pool() as pool:
    result = pool.map(square, [1, 2, 3, 4, 5])
    print(result)

# Output:
# [1, 4, 9, 16, 25]
```

## Project: Advanced Python Concepts

In this project, you will implement advanced Python concepts to enhance your coding skills.

### Part 1: Decorators

1. Create a set of functions to be used as decorators.
2. Apply decorators to functions in a sample program.

### Part 2: Generators

1. Implement a generator that generates a sequence of prime numbers.
2. Use the generator to perform a task, such as finding the sum of the first 100 prime numbers.

### Part 3: Concurrency

1. Explore threading or multiprocessing by parallelizing a task.
2. Compare the performance with and without concurrency.

### Bonus:

- Combine decorators and generators in a more complex program.
- Experiment with different concurrency scenarios and measure their impact on performance.

**Tip**: You can find the documentation for the `threading` module here: https://docs.python.org/3/library/threading.html and the `multiprocessing` module here: https://docs.python.org/3/library/multiprocessing.html
