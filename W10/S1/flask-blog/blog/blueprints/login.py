from flask import Blueprint, render_template,request ,redirect,session
from blog.db import get_db
import sqlite3

# define our blueprint
login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods =['POST','GET'])
def login():
    if request.method == "GET":
        # render the login template
        return render_template('login/login.html')
    else:
        # read values from the login form
        username= request.form['username']
        password = request.form['password']

        # get the DB connection
        db = get_db()
        
        # insert user into db
        try:
            # get user by username
            user= db.execute('SELECT * FROM user WHERE username LIKE ?',(username,)).fetchone()
            # check if username exists
            if user  != None:
                # check if credentials are valid
                if user['username'] == username and user['password'] == password:
                    # store the user ID in the session  
                    session['uid']= user['id']  
                    session['username'] = user['username']
                    return redirect("/posts")

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            return redirect("/404")

@login_bp.route('/session')
def show_session():
    return dict(session)

@login_bp.route('/logout')
def logout():
    # pop 'uid' from session
    session.clear()

    # redirect to index
    return redirect("/")