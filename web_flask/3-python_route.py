#!/usr/bin/python3
'''A script that starts a Flask application
'''
from flask import Flask


app = Flask(__name__)
'''The flask application instance'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''The home route'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''The hbnb route'''
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    '''The c route'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python(text):
    '''The python route'''
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
