#!/usr/bin/python3
""" Routes to / """
from flask import Flask

APP = Flask(__name__)


@APP.route("/", strict_slashes=False)
def hello():
    """A route to /"""
    return "Hello HBNB!"


@APP.route("/hbnb", strict_slashes=False)
def hbnb():
    """A route to /hbnb"""
    return "HBNB"


@APP.route("/c/<text>", strict_slashes=False)
def c(text):
    """Route to /c"""
    if "_" in text:
        text = text.replace("_", " ")
    return "C {text}".format(text=text)


@APP.route("/python/")
@APP.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Route to /python"""
    if "_" in text:
        text = text.replace("_", " ")
    return "Python {text}".format(text=text)


@APP.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display number if its int"""
    return "{n} is a number".format(n=n)


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
