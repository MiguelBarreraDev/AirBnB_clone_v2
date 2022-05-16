#!/usr/bin/python3
"""
task: HBNB
Write a script that starts a Flask web application that listening on
host: 0.0.0.0 & post: 5000
"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
