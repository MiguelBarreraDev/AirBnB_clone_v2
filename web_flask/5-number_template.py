#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask, render_template

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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_view(text="is cool"):
    """Definition the view function that return a message"""
    text = text.replace("_", " ")
    return "Python " + text


@app.route("/number/<int:n>", strict_slashes=False)
def number_view(n):
    """Definition the view function that validate if n is a number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_view(n):
    """Definition the view function that render a template"""
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
