#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template
from models.__init__ import storage

app = Flask(__name__, static_url_path="")


@app.teardown_appcontext
def appcontext(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def display_page():
    """Display a HTML page like 6-index.html, HBNB filters"""
    from models.state import State
    from models.amenity import Amenity
    all_states = storage.all(State).values()
    all_amenities = storage.all(Amenity).values()
    data = {
        "states": all_states,
        "amenities": all_amenities
    }
    return render_template("10-hbnb_filters.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
