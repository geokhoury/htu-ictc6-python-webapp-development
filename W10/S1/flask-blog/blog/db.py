import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """

    # connect to the DB if there is no connection already
    if 'db' not in g:
        # connect to sqlite3
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    # return the DB connection
    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """

    # pop db connection from g
    db = g.pop('db', None)

    # if db connection is still open, close it
    if db is not None:
        db.close()


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    # initialize the database from the schema
    init_db()

    # print message to the user
    click.echo('Initialized the database. Your database is now ready :).')


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)