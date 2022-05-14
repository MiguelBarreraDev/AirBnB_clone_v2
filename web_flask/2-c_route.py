#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home_view():
    """Definition the view function for the rule root"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_view():
    """Definition the view function for the rule hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_view(text):
    """Definition the view function that return a message"""
    text = text.replace("_", " ")
    return "C " + text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
