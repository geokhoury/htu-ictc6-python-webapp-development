from flask import Flask, render_template, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class NameForm(FlaskForm):
    name = StringField('What is your name?', [validators.InputRequired()]) 
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST']) 
def index():

    # create an instance of our NameForm
    form = NameForm()

    # handle form submission
    if form.validate_on_submit():

        # read 'name' from session
        old_name = session.get('name')      # 'the old name' or None

        # check if the name has changed
        if old_name is not None and old_name != form.name.data:
            # run like the Flash...
            flash('Looks like you have changed your name!') 
        
        # store the name in the session
        session['name'] = form.name.data

        # clear the name field in the form
        form.name.data = ''

        # reload the index page
        return redirect(url_for('index'))

    # render the index template with form and name
    return render_template('index.html', form = form, name = session.get('name'))

@app.route('/clear')
def clear_session():
    # clear all session values
    session.clear()

    # Flash message for clearing the session
    flash('Session cleared.') 
    return redirect(url_for('index'))
