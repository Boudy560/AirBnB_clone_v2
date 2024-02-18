#!/usr/bin/python3
""" 2. Script to start a Flask web applicalication with 3 view functions """

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


if __name__ == '__main__':
    applica.run(host='0.0.0.0', port=5000)
