from flask import Flask, request, url_for
import math

app = Flask(__name__)

# Route for path /
@app.route('/')
def index():
    return 'I am the index page.'
    
# Route for path /hello/<name>
@app.route('/hello/<name>')
def say_hello(name):
    return f'<h1>Hello, {name.title()}!</h1>'

# Multiple routes for a function
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=None):
    if name:
        return f"Welcome, {name.title()}!"
    else:
        return f"Welcome to Flask!"


# Route for path /even_odd/<int:number>
@app.route('/even_odd/<int:number>')
def even_odd(number):
    if number % 2 ==0:
        return f'{number} is even.'
    else:
        return f'{number} is odd.'

# Route for path /sum/<int:number>
@app.route('/sum/<int:number>')
def sum_numbers(number):
    numbers = range(1, number + 1)
    sum_numbers = sum(numbers)

    return f"The sum of {list(numbers)} is {sum_numbers}."

# Route for path /pi/<float:number>
@app.route('/pi/<float:number>')
def bigger_smaller_pi(number):
    if number <= math.pi:
        return f"{number} is less than PI by {math.pi - number}."
    else:
        return f"{number} is greater than PI by {number - math.pi}."

# Route for path /headers
@app.route('/headers')
def request_headers():
    # Read the HTTP request headers
    request_headers = request.headers
    # Cast and return the values as a dictionary
    return dict(request_headers)

# Route for path /which_browser 
@app.route('/browser')
def which_browser():
    # Read the 'User-Agent' value from the HTTP request headers
    user_agent = request.headers.get('User-Agent')
    return f'You are using <b>{user_agent}</b> to access this page.'

with app.test_request_context():
    print(f"The URL for index() is: {url_for('index')}")
    print(f"The URL for which_browser() is: {url_for('which_browser')}")