"""
Lis of views available for the titanic application.
Stores also demo views simply for the pleasure of coding.
"""

from flask import render_template
from flask_classful import FlaskView, route
from forms import TitanicUserForm

class DemoView(FlaskView):
    def index(self):
        html = "<a href='./titanic/add'> Add a record </a>"
        return 'Hello World!<br>' + html

    @route('/<name>')
    def template(self, name):
        return render_template('index.html', name=name)

class TitanicView(FlaskView):

    # Target : http://localhost:5000/titanic
    def index(self):
        return "<h1>Here we should list titanic records</h1>"

    @route('/add')
    def addTitanicRecord(self):
        form = TitanicUserForm()
        return render_template('titanic.html', form=form)

