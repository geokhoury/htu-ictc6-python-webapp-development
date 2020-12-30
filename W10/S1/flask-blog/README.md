# Flask Blog

This project is a very simple version of the flask blog app in http://flask.pocoo.org/docs/1.0/tutorial/

## Project setup

* Clone the project files.
* Create a virtual environment.
  * You need Python 3.6 or higher.
  * Install the requirements (`python -m pip install -r requirements.txt`).

## Run the blog app

On a **Windows** command prompt, run the following commands:

```sh
$ set FLASK_APP="blog"
$ set FLASK_ENV="development"
$ flask init-db
$ flask run
```

On a **Mac** or **Linux** terminal, run the following commands:

```sh
$ export FLASK_APP=blog
$ export FLASK_ENV=development
$ flask init-db
$ flask run
```

In a web browser, go to [http://127.0.0.1:5000/]