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

@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pytext(text="is cool"):
    """displays Python followed by value of
    text if provided else is cool
    """
    res = text.replace('_', ' ')
    return "Python " + res

@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """displays n is a number only if n is int
    """
    s = str(n)
    res = " is a number"
    return s + res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
