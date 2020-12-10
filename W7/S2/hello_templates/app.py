from flask import Flask
from flask import render_template
from flask import url_for

import random

app = Flask(__name__)  # create a new flask application

# define basic routes
@app.route('/')
def render_index():
    menu = [{"title":"Home", "url":url_for("render_index")},
            {"title":"Hello", "url":url_for("say_hello")},
            {"title":"Greet", "url":url_for("greet")},
            {"title":"Magic 8", "url":url_for("magic_8")}
        ]
    return render_template("index.html", global_style=url_for("static", filename="style.css"), menu = menu)


@app.route('/hello/')
def say_hello():
    return render_template("hello.html", go_home=url_for("render_index"))


@app.route('/magic8')
def magic_8():
    rndx = random.randint(1, 10)
    return render_template("magic8.html", global_style=url_for("static", filename="style.css"), random_number=rndx)


@app.route('/greet/')
@app.route('/greet/<name>')
def greet(name=None):
    return render_template('greet.html', name=name, go_home=url_for("render_index"))


# run your flask application

if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)  # run the flask app
