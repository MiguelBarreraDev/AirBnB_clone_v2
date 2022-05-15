#!/usr/bin/python3
"""
task: Number template
Write a script that starts a Flask web application that listening on
host: 0.0.0.0 & post: 5000
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    View function for the '/' rule that return a message
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb_view():
    """
    View function for the '/hbnb' rule that return a message
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_view(text):
    """
    View function for the '/c/<text>' dinamyc rule that return a message
    """
    return ("C " + text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_view(text="is cool"):
    """
    View function for the dinamyc rule '/python/<text>' that
    return a message
    """
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number_view(n):
    """
    View function for the dinamyc rule '/number/<int:n>' that
    return a message with the n value
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_view(n):
    """
    View function for the dinamyx rule '/number_template/<int:n>'
    that return a template
    """
    return render_template("5-number.html", data={"number": n})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
