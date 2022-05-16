#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template
from models.__init__ import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def appcontext(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<_id>", strict_slashes=False)
def display_page(_id=None):
    """Display page html"""
    dict_states = storage.all(State)
    found = None
    key = None
    if _id:
        key = "State" + "." + str(_id)
        if key in dict_states.keys():
            found = 1
    data = {
        "content": dict_states[key] if found == 1 else dict_states.values(),
        "id": _id,
        "found": found
    }
    return render_template("9-states.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
