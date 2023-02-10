"""
Python Titanic.
Target of this main application is to launch a web app available on port 5000.

 - / : simple hello world
 - /<name> : simple hello <name> sending data via URL
 - /titanic/ : list all records available in the titanic DB
 - /titanic/add : add a record to the titanic DB
 - /titanic/edit/<id> : edit a record in the titanic DB
 - /titanic/delete/<id> : remove a record in the titanic DB
"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import database
from views import *

if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'this is a secret'
    Bootstrap(app)
    database.create_db_if_not_exists('database.sqlite')
    DemoView.register(app, route_base='/')
    TitanicView.register(app, route_base='/titanic')
    app.run(debug=True)