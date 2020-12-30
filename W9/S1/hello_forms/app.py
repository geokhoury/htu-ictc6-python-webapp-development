from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class HelloForm(FlaskForm):
    name = StringField('What is your name?', [validators.InputRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():

    # created an instance of our form
    hello_form = HelloForm()

    # check if it is a form submission
    if hello_form.validate_on_submit():
        # read the name from the form submission
        name = hello_form.name.data
        
        # render the greet template with the name
        return render_template('greet.html', name = name)

    # render the index template with the form
    return render_template('index.html', form = hello_form)