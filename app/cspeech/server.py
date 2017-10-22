# server.py
from flask import Flask, render_template, flash, request, redirect
from flask_script import Manager

app = Flask(__name__)
app.config['SECRET_KEY'] = "hard"
manager = Manager(app)

@app.route('/', methods=["GET", "POST"])
def index():
    print("TEST")
    if request.method == "POST":
        print("POST")
        response = request.form["phone"]
        print(response)
        return "HELLO"
    return render_template("index.html")

@app.route('/getVideo')
def video():
    print("VIDEO")
    return jsonify("https://www.handspeak.com/word/b/baby.mp4")

if __name__ == "__main__":
    manager.run()
