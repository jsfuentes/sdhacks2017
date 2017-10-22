# server.py
from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
manager = Manager(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    return render_template("test2.html")

if __name__ == "__main__":
    manager.run()
