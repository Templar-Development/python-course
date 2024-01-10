# Lesson-8 | Ensuring Code Quality

## 1. Testing Basics (unittest or pytest)

### Introduction to Unit Testing

Unit testing is the process of testing individual units or components of a software. It ensures that each part of a program is working as designed.

### Writing and Running Basic Test Cases

Use unittest or pytest to write and run basic test cases for your functions.

Example (unittest):

```python
# Testing basics with unittest
import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        # code to test , expected result
        self.assertEqual(add(2, 3), 5) 
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

Example (pytest):

```python
# Testing basics with pytest
def add(a, b):
    return a + b

def test_add():
    # code to test result = expected result
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

### Test Fixtures and Test Suites

Use test fixtures to set up preconditions for your tests and create test suites to organize multiple test cases.

Example (unittest):

```python
# Test fixtures and test suites with unittest
import unittest

class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        # Set up fixtures if needed
        pass

    def tearDown(self):
        # Clean up after the test
        pass

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

# Create a test suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMathFunctions('test_add'))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
```

## 2. Debugging Techniques

### Identifying and Fixing Common Errors

Understand common errors (syntax errors, logical errors) and apply systematic approaches to identify and fix them.

### Using Print Statements for Debugging

Insert print statements strategically to trace the flow of your program and inspect variable values.

Example:

```python
# Using print statements for debugging
def divide(a, b):
    print(f'Dividing {a} by {b}')
    result = a / b
    print(f'Result: {result}')
    return result
```

### Utilizing Debugging Tools (e.g., pdb)

Use Python's built-in debugger (pdb) to step through your code and inspect variables at runtime.

Example:

```python
# Utilizing pdb for debugging
import pdb

def divide(a, b):
    pdb.set_trace()
    result = a / b
    return result
```

## Project: Testing and Debugging

In this project, you will focus on ensuring code quality through testing and debugging.

### Part 1: Testing with unittest or pytest

1. Write test cases for functions from previous projects (e.g., calculator, hangman game).
2. Execute the tests and ensure all cases pass.

### Part 2: Debugging

1. Introduce intentional bugs into a small program.
2. Use debugging techniques (print statements, debugging tools) to identify and fix the issues.

### Bonus:

- Explore more advanced testing concepts (e.g., mocking) and debugging tools.
- Implement test coverage analysis to ensure thorough testing.

**Tip:** You can find the documentation for unittest here: https://docs.python.org/3/library/unittest.html and pytest here: https://docs.pytest.org/en/stable/
