# Lesson-7 | Database Interaction with Python

## 1. Database Basics (SQLite or Similar)

### Introduction to Databases

Databases are organized collections of data, typically stored electronically. They provide an efficient way to manage and retrieve information.

### Overview of SQLite

SQLite is a lightweight, serverless, and self-contained relational database engine. It's a popular choice for small to medium-sized applications.

### Creating and Connecting to a Database

Use SQLite to create a database and connect to it from Python.

Example:

```python
# Creating and connecting to a SQLite database
import sqlite3

# Connect to or create a database
conn = sqlite3.connect('my_database.db')
```

## 2. SQL Basics (CRUD Operations)

### Understanding SQL (Structured Query Language)

SQL is a domain-specific language for managing relational databases. It includes commands for CRUD operations (Create, Read, Update, Delete).

### Performing CRUD Operations (Create, Read, Update, Delete)

Use SQL commands to interact with the database.

Example:

```python
# SQL CRUD operations
# Create
conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

# Read
result = conn.execute('SELECT * FROM users').fetchall()

# Update
conn.execute('UPDATE users SET age = 25 WHERE id = 1')

# Delete
conn.execute('DELETE FROM users WHERE id = 2')
```

### Using SQL in Python with SQLite

Execute SQL queries from Python using the `execute` method.

Example:

```python
# Using SQL in Python with SQLite
# Insert data
conn.execute("INSERT INTO users (name, age) VALUES ('John', 30)")

# Fetch data
result = conn.execute('SELECT * FROM users').fetchall()
```

## 3. Integrating Databases with Python

### Connecting Python to a Database

Use the `sqlite3` module to connect Python to a SQLite database.

Example:

```python
# Connecting Python to a SQLite database
import sqlite3

conn = sqlite3.connect('my_database.db')
```

### Executing SQL Queries from Python

Use the `execute` method to run SQL queries from Python.

Example:

```python
# Executing SQL queries from Python
conn.execute('CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL)')

conn.execute("INSERT INTO products (name, price) VALUES ('Laptop', 1200.0)")

result = conn.execute('SELECT * FROM products').fetchall()
```

### Managing Database Connections

Close database connections to free up resources.

Example:

```python
# Managing database connections
conn.close()
```

## Project: Simple Database Interaction

In this project, you will apply your knowledge of databases by creating a Python program that interacts with a database.

### Requirements:

1. Create a SQLite database with a table of your choice (e.g., for storing user information).
2. Write Python functions to perform CRUD operations on the database.
3. Implement a simple user interface in the console to interact with the database.

### Bonus:

- Implement error handling for database operations.
- Explore more advanced database concepts, such as indexing and transactions.

**Tip:** You can find the documentation for the `sqlite3` module here: https://docs.python.org/3/library/sqlite3.html
