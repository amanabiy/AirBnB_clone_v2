#!/usr/bin/python3
"""
Flask web frame work
"""
from flask import Flask
from flask.templating import render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Say hello """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ say hnbn """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Displays C plus the text entered """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    """ Python plus a given text """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """ Displays n is a number """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def display_page_if_int(n):
    """" Displays the template if n is an integer """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def display_page_int_parity(n):
    """ Displays page if int and with the parity check """
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, parity='even')
    else:
        return render_template('6-number_odd_or_even.html', n=n, parity='odd')


@app.teardown_appcontext
def tear_down(self):
    """after each request remove current SQLAlchemy session"""
    storage.close()


@app.route('/states_list')
def html_fetch_states():
    """display html page
       fetch sorted states to insert into html in UL tag
    """
    states = [s for s in storage.all("State").values()]
    return render_template('7-states_list.html',
                           states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)