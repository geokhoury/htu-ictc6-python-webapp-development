from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user_info/<name>/<int:age>')
def show_user_information(name, age):
    return render_template('user.html', name=name, age=age)

@app.route('/add/<int:x>/<int:y>')
def add(x,y):
    return render_template('addition.html', value1=x, value2=y, sum = x+y)

@app.route('/divide/<int:x>/<int:y>')
def divide(x,y):
    return render_template('division.html', n1=x, n2=y)

@app.route('/favourites/<name>')
@app.route('/favourites')
def favourite_topics(name=None):
    topics = ['functions', 'classes', 'OOP', 'decorators', 'Flask']
    return render_template('favourites.html', topics=topics, name=name)