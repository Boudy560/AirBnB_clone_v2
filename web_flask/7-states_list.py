#!/usr/bin/python3
""" 7. Start flask service that does something. """

from flask import Flask
from flask import render_template


applica = Flask(__name__)
applica.url_map.strict_slashes = False


#@applica.routett()


if __name__ == '__main__':
    applica.run(host='0.0.0.0', port=5000)
