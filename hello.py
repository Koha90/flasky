from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    """
    index: function for render html
    """
    return "<h1>Hello world, from flask</h1>"


@app.route("/user/<name>")
def user(name):
    """
    user: function for rendering html with
    """
    return f"<h2>Hello, {name}!"


app.add_url_rule("/", "index", index)
