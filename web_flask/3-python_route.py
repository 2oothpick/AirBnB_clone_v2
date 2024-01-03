#!/usr/bin/python3
""" Scripts starts a Flask web app """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """ Returns HBNB """
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_hbnb2():
    return "HBNB"


@app.route("/c/<text>/")
def show_text(text):
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route("/python")
@app.route("/python/<text>/")
def show_python(text="is cool"):
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
