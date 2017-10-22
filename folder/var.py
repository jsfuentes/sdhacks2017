from flask import Flask, render_template, flash, request, redirect

app = Flask(__name__)\

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        response = request.form["response"]
        return render_template("variable.html", variable = response)
    return render_template("login.html")

if __name__ == "__main__":
    app.run()
