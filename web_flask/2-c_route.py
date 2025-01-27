#!/usr/bin/python3
"""web application be listening on 0.0.0.0, port 5000"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB'
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display C followed by text variable"""
    return "C " + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
