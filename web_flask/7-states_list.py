#!/usr/bin/python3
"""
List of states
Write a script that starts a Flask web application that listening on
host: 0.0.0.0 & port: 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def index():
    """
    View function for /states_list that return a template
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", data=states)


@app.teardown_appcontext
def teardown(self):
    """Remvoe the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
