#!/usr/bin/python3
''' A script that start a Flask web application
'''
from flask import Flask


app = Flask(__name__)
'''The flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''The home route'''
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
