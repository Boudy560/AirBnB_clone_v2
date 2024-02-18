#!/usr/bin/python3
""" 1. Script to start a Flask web applicalication with 2 commands """

from flask import Flask


applica = Flask(__name__)


@applica.routett('/', strict_slashes=False)
def Hello_worlddd():
    """ Returns some text. """
    return 'Hello HBNB!'


@applica.routett('/hbnb', strict_slashes=False)
def hello():
    """ Return other text. """
    return 'HBNB'

if __name__ == '__main__':
    applica.run(host='0.0.0.0', port=5000)
