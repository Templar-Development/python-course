# Lesson-4 | Python Beyond the Basics

## 1. Modules and Packages

### Organizing Code into Modules

Modules are Python files containing reusable code. Use `import` to access functions or variables from a module.

Example:

```python
# Module: my_module.py
def greet(name):
    return f"Hello, {name}!"

# Another file
import my_module
result = my_module.greet("Alice")
```

### Creating and Using Packages

Packages are directories containing multiple modules. They include an `__init__.py` file.

Example:

```
my_package/
|-- __init__.py
|-- module1.py
|-- module2.py
```

### Importing Modules and Packages

Use `import` to bring in modules or packages. You can use aliases for shorter names.

Example:

```python
# Importing modules/packages
import my_module
from my_package import module1 as m1
```

## 2. Virtual Environments

### Understanding the Need for Virtual Environments

Virtual environments isolate project dependencies, preventing conflicts with system-wide packages.

### Creating and Activating Virtual Environments

Use `venv` or `virtualenv` to create virtual environments. Activate them using the appropriate command for your operating system.

Example (using `venv`):

```bash
# Creating a virtual environment
python -m venv myenv

# Activating the virtual environment
source myenv/bin/activate  # On Unix or MacOS
myenv\Scripts\activate  # On Windows
```

### Managing Dependencies with `requirements.txt`

List project dependencies in a `requirements.txt` file for easy installation.

Example `requirements.txt`:

```
numpy==1.20.3
matplotlib==3.4.2
```

## 3. Introduction to External Libraries

### Exploring Popular External Libraries

Python has a rich ecosystem of libraries. Some popular ones include NumPy, Pandas, Matplotlib, and more.

### Installing External Libraries Using pip

Use `pip` to install external libraries.

Example:

```bash
pip install numpy
```

### Basic Usage of NumPy for Numerical Operations

NumPy provides powerful tools for working with arrays, mathematical functions, and linear algebra.

Example:

```python
# Using NumPy
import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Performing numerical operations
result = arr1 + arr2
```

## Project: Using External Libraries - NumPy

In this project, you will apply your knowledge of external libraries by working with NumPy, a powerful library for numerical operations in Python.

### Requirements:

1. Install NumPy using pip.
2. Create a program that generates and manipulates arrays using NumPy.
3. Perform basic numerical operations (e.g., addition, subtraction, multiplication) on arrays.
4. Explore and demonstrate some advanced features of NumPy.

### Bonus:

- Investigate and implement array manipulation functions provided by NumPy.
- Create a simple data visualization using NumPy arrays and Matplotlib.

**Tip:** You can find the documentation for NumPy here: https://numpy.org/doc/stable/
