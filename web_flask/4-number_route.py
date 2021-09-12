#!/usr/bin/python3
"""
Flask web frame work
"""
from flask import Flask
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
