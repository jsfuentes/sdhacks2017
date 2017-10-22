from flask import Flask, render_template, flash, request, redirect

app = Flask(__name__)\
app.config['SECRET_KEY'] = "hard"

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        response = request.form["response"]
        if response == "hello":
            return render_template("abc.html")
    return render_template("login.html")

if __name__ == "__main__":
    app.run()
