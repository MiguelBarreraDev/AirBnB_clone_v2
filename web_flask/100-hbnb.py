#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template
from models.__init__ import storage

app = Flask(__name__, static_url_path="")


@app.teardown_appcontext
def appcontext(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def display_page():
    """Display a HTML page like 6-index.html, HBNB filters"""
    from models.state import State
    from models.amenity import Amenity
    from models.place import Place
    all_states = storage.all(State).values()
    all_amenities = storage.all(Amenity).values()
    all_places = storage.all(Place).values()
    print(all_places)
    data = {
        "states": all_states,
        "amenities": all_amenities,
        "places": all_places
    }
    return render_template("./100-hbnb.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
