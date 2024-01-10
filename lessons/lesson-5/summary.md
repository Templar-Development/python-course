# Lesson-5 | Mastering Python Techniques

## 1. Regular Expressions

### Introduction to Regular Expressions

Regular expressions (regex) are sequences of characters defining a search pattern. They are powerful tools for string manipulation and pattern matching.

### Basic Pattern Matching

Use regex to find specific patterns in text, such as matching digits, letters, or special characters.

Example:

```python
# Basic pattern matching
import re

pattern = r'\d+'  # Matches one or more digits
text = 'The price is $20 and $30.'
matches = re.findall(pattern, text)

# Result: ['20', '30']
```

### Using Regex in Python (re module)

The `re` module in Python provides functions for working with regular expressions, including `findall`, `search`, and more.

Example:

```python
# Using regex in Python
import re

pattern = r'\b\d{3}-\d{2}-\d{4}\b'  # Matches social security numbers
text = 'User's SSN: 123-45-6789'
result = re.search(pattern, text)

# Result: <re.Match object; span=(12, 24), match='123-45-6789'>
```

## 2. Lambda Functions

### Creating Anonymous Functions with Lambda

Lambda functions are concise, anonymous functions defined using the `lambda` keyword.

Example:

```python
# Lambda function
square = lambda x: x**2
result = square(4)  # Result: 16
```

### Use Cases for Lambda Functions

Lambda functions are useful for short-term, one-time use, often in functions like `map`, `filter`, and `sorted`.

Example:

```python
# Using lambda with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

# Result: [1, 4, 9, 16, 25]
```

### Combining Lambda with Functions like `map` and `filter`

Lambda functions work well with functions like `map` and `filter` for concise and readable code.

Example:

```python
# Using lambda with filter
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Result: [2, 4]
```

## 3. Map, Filter, and Reduce

### Utilizing the `map` Function

The `map` function applies a specified function to all items in an iterable.

Example:

```python
# Using map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

# Result: [1, 4, 9, 16, 25]
```

### Filtering Elements with `filter`

The `filter` function filters elements based on a specified function.

Example:

```python
# Using filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

### Reducing Sequences with `reduce`

The `reduce` function from the `functools` module applies a rolling computation to sequential pairs of values.

Example:

```python
# Using reduce
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
```

## Project: Text Processing with Regular Expressions

In this project, you will apply regular expressions to perform text processing tasks. This will enhance your understanding of pattern matching and the practical use of regular expressions in Python.

### Requirements:

1. Create a program that validates and processes user-inputted text using regular expressions.
2. Implement regex patterns to validate email addresses, phone numbers, or other user-defined patterns.
3. Use regex to extract specific information from a given text.

### Bonus:

- Apply regular expressions to search and replace text in a file.
- Explore more complex regex patterns for advanced text processing tasks.

**Tip:** You can find the documentation for the `re` module here: https://docs.python.org/3/library/re.html and you can test your regex patterns here: https://regex101.com/
