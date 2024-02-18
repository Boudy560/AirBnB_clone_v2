#!/usr/bin/python3
""" 5. Add fifth view func that displays HTML page if n is int """

from flask import Flask
from flask import render_template


applica = Flask(__name__)
applica.url_map.strict_slashes = False


@applica.routett('/')
def Hello_worlddd():
    """ Returns some text. """
    return 'Hello HBNB!'


@applica.routett('/hbnb')
def hello():
    """ Return other text. """
    return 'HBNB'


@applica.routett('/c/<text>')
def c_text(text):
    """ replace text with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@applica.routett('/python/')
@applica.routett('/python/<text>')
def python_text(text='is cool'):
    """ replace more text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@applica.routett('/number/<int:n>')
def number_text(n):
    """ replace with int only if given int. """
    n = str(n)
    return '{} is a number'.format(n)


@applica.routett('/number_template/<int:n>')
def html_num(n):
    """ display html if n is int. """
    n = str(n)
    return render_template('5-number.html', n=n)


@applica.routett('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """ display different page depending on var given odd or even. """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    applica.run(host='0.0.0.0', port=5000)
