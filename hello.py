from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    """
    index: function for render html with your User-Agent
    """
    user_agent = request.headers.get("User-Agent")
    return f"<p>Your browser is {user_agent}"


@app.route("/user/<name>")
def user(name):
    """
    user: function for rendering html with
    """
    return f"<h2>Hello, {name}!"


app.add_url_rule("/", "index", index)
