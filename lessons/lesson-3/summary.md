# Lesson-3 | Enhancing Your Python Skills

## 1. Exception Handling

### Understanding Exceptions

Exceptions are events that occur during the execution of a program that disrupts the normal flow of instructions.

### `try`, `except`, `finally` Blocks

Use `try` to enclose the code that might raise an exception, `except` to handle the exception, and `finally` for code that must be executed, regardless of whether an exception occurred.

Example:

```python
# Exception handling with try, except, finally
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")
```

### Handling Specific Exceptions

Handle different exceptions separately based on the error type.

Example:

```python
# Handling specific exceptions
try:
    value = int("abc")
except ValueError:
    print("Invalid conversion to integer.")
except TypeError:
    print("Incorrect type.")
```

## 2. Object-Oriented Programming Basics

### Classes and Objects

Classes are blueprints for objects. Objects are instances of a class.

Example:

```python
# Class definition
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object
my_dog = Dog("Buddy", 3)
```

### Attributes and Methods

Attributes are characteristics of an object, and methods are functions associated with an object.

Example:

```python
# Attributes and methods
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2
```

### Constructors and Destructors

The `__init__` method is a constructor, used for initializing object attributes. The `__del__` method is a destructor, used for cleaning up resources.

Example:

```python
# Constructors and destructors
class MyClass:
    def __init__(self):
        print("Object created!")

    def __del__(self):
        print("Object destroyed!")
```

## Project: Simple Bank Account System

In this project, you will create a basic bank account system using object-oriented programming principles. This project aims to reinforce your understanding of classes, objects, and exception handling.

### Requirements:

1. Create a `BankAccount` class with attributes like account number, balance, and account holder name.
2. Implement methods for deposit, withdrawal, and checking the account balance.
3. Use exception handling to manage cases such as insufficient funds.
4. Test your bank account system with various transactions.

### Bonus:

- Extend the project to include multiple account types (e.g., savings, checking).
- Implement additional features such as transferring funds between accounts.
