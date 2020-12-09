from flask import Flask
import random

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route using the route decorator
@app.route('/') 
def hello_world():
    return 'Hello, World!'

@app.route('/helloagain')
def hello_again():
    return 'Hello, again :)!'

@app.route('/hellohtml')
def my_html():
    return '<h1>Hello, HTML.</h1> <p>I am an HTML element.</p>'

@app.route('/magic_number')
def my_magic_number():
    random_number = random.randint(1, 6)
    return f'Your magic number is: {random_number}'
