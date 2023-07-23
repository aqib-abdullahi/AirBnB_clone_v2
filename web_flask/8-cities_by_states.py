#!/usr/bin/python3
"""web application be listening on 0.0.0.0, port 5000"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

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

@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """Display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd_or_even(n):
    """display a HTML page only if n is
    even|odd inside the tag BODY
    """
    if (n % 2) == 0:
        d = "even"
    else:
        d = "odd"
    return render_template('6-number_odd_or_even.html', n=n, d=d)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page of the States
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page of the States and the
    Cities by State
    """
    states = storage.all(State).values()
    cities = list()

    for state in states:
        for city in state.cities:
            cities.append(city)

    return render_template('8-cities_by_states.html',
                           states=states, state_cities=cities)

@app.teardown_appcontext
def teardown_database(error):
    """Closes the database again at the end of the request.
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
