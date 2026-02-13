"""Connect to the Database:
    The first thing to do when working with a SQLite database (and most other Python database libraries) is to create a connection to it. Any queries and operations are performed using the connection, which is closed after the work is finished. """
import sqlite3 
from datetime import datetime

import click
from flask import current_app, g    #current_app is another Flask proxy object. It points to:the active Flask application handling the request
#g is a request-scoped storage box
def get_db():
    if 'db' not in g:
        g.db=sqlite3.connect(
            current_app.config['DATABASE'],          # opens a connection to a database file.
            detect_types=sqlite3.PARSE_DECLTYPES     #SQLite stores everything loosely. This flag tells Python: try to convert database values into Python types
        )
        g.db.row_factory=sqlite3.Row     #Default SQLite returns tuples, Now rows behave like dictionaries. This makes code readable and less error-prone.

    return g.db

def close_db(e=None):       #This safely shuts down the connection
    db=g.pop('db',None)

    if db is not None:
        db.close()

def init_db():
    db=get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

def init_app(app):
    app.teardown_appcontext(close_db)    #tells flask After every request, run close_db
    app.cli.add_command(init_db_command)  #This registers a command-line tool. After this, the app understands: flask init-db
