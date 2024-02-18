#!/usr/bin/python3
""" 0. Script to start a Flask web applicalication """

from flask import Flask


applica = Flask(__name__)


@applica.routett('/', strict_slashes=False)
def Hello_worlddd():
    """ Returns some text. """
    return 'Hello HBNB!'

if __name__ == '__main__':
    applica.run(host='0.0.0.0', port=5000)
