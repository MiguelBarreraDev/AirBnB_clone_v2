#!/usr/bin/python3
"""
Hello Flask!
Write a script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """
    Starts a Flask web aplication that listening on
    Host: 0.0.0.0 & port: 5000
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
