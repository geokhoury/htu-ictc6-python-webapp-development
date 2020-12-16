# calcweb

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)               # create a new flask application

# define basic routes

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'GET':
        # render the add page
        return render_template("add.html")
    else:
        print("The page was requested with the method POST.")

        # read the values from the form
        n1 = int(request.form['n1'])   # read the value from the first number input
        n2 = int(request.form['n2'])  # read the value from the second number input

        return redirect(url_for("result", n1 = n1, n2 = n2, operation = 'add', answer = n1 + n2))

@app.route("/subtract", methods=['GET', 'POST'])
def subtract():
    if request.method == 'GET':
        # render the subtract method
        return render_template("subtract.html")
    else:
        # read and cast the values from the form
        number1 = int(request.form['n1'])
        number2 = int(request.form['n2'])

        # subtract the values
        result = number1 - number2

        # redirect the user to the result page
        return redirect(url_for("result", answer = result, operation = 'subtract'))
        
@app.route("/multiply")
def multiply():
    return render_template("multiply.html")

@app.route("/divide")
def divide():
    return render_template("divide.html")

@app.route("/")
def index():
    my_menu = [
        {"title":"Add", "url":url_for('add')},
        {"title":"Subtract", "url":url_for('subtract')},
        {"title":"Multiply", "url":url_for('multiply')},
        {"title":"Divide two numbers", "url":url_for('divide')}
    ]
    return render_template("index.html", menu = my_menu)

@app.route("/result/<n1>/<n2>/<operation>/<int:answer>")
def result(n1, n2, operation, answer):
    return render_template("result.html", n1 = n1, n2= n2, operation = operation, result=answer)


# run your flask application

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)           # run the flask app
