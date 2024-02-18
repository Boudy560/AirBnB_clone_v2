#!/usr/bin/python3
""" 4. Add fourth view function that displays var only if is integer """

from flask import Flask


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


if __name__ == '__main__':
    applica.run(host='0.0.0.0', port=5000)
