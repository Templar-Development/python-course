# Lesson-6 | Web Interaction with Python

## 1. Web Scraping Basics

### Introduction to Web Scraping

Web scraping is the process of extracting data from websites. BeautifulSoup is a Python library for pulling data out of HTML and XML files.

### Understanding HTML Structure

HTML (Hypertext Markup Language) is the standard markup language for creating web pages. Understanding its structure is crucial for effective web scraping.

### Basic Web Scraping with BeautifulSoup

Use BeautifulSoup to parse HTML and extract information from web pages.

Example:

```python
# Web scraping with BeautifulSoup
from bs4 import BeautifulSoup
import requests

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting data
title = soup.title.text
paragraphs = soup.find_all('p')
```

## 2. API Usage (Requests Library)

### Overview of APIs

APIs (Application Programming Interfaces) allow different software applications to communicate with each other. They provide a set of rules for building software.

### Making HTTP Requests with the `requests` Library

The `requests` library simplifies sending HTTP requests.

Example:

```python
# Making HTTP requests with the requests library
import requests

url = 'https://api.example.com/data'
response = requests.get(url)

# Accessing data from the response
data = response.json()
```

### Handling API Responses

Handle API responses, which often come in JSON format, to extract and use the desired information.

Example:

```python
# Handling API responses
if response.status_code == 200:
    data = response.json()
    # Process the data here
else:
    print(f"Error: {response.status_code}")
```

## 3. Introduction to Flask (Web Framework)

### Setting Up a Basic Flask Application

Flask is a lightweight web framework for Python. Create a basic Flask app with routes and views.

Example:

```python
# Setting up a basic Flask application
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'
```

### Routing and Views in Flask

Define routes and views to handle different URLs and display content.

Example:

```python
# Routing and views in Flask
@app.route('/about')
def about():
    return 'This is the About page.'
```

### Handling User Input with Forms

Use Flask to handle user input through forms.

Example:

```python
# Handling user input with forms in Flask
from flask import Flask, request

@app.route('/submit', methods=['POST'])
def submit_form():
    user_data = request.form['data']
    # Process user input
    return 'Form submitted!'
```

## Project: Simple Web Scraping and Flask Web App

In this project, you will explore both web scraping and web development using Flask.

### Part 1: Web Scraping

1. Choose a website with public data.
2. Use BeautifulSoup to scrape and extract information from the website.

### Part 2: Flask Web App

1. Create a Flask web application.
2. Display the scraped information on a webpage.
3. Add a form for users to input data and display the results.

### Bonus:

- Implement error handling in your web scraping and Flask application.
- Add more features to your Flask app, such as additional routes and dynamic content.

**Tip:** You can find the documentation for the `requests` library here: https://requests.readthedocs.io/en/master/ and the documentation for Flask here: https://flask.palletsprojects.com/en/1.1.x/
