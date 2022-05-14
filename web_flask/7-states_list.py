#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_page():
    """Display page html"""
    all_states = storage.all('State').values()
    return render_template("7-states_list.html", states=all_states)


@app.teardown_appcontext
def appcontext(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
