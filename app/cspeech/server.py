# server.py
from flask import Flask, render_template, flash, request, redirect
from flask_script import Manager
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = "hard"
manager = Manager(app)

client = MongoClient("mongodb://admin:admin1@ds227555.mlab.com:27555/sdhacks2017")
db = client.sdhacks2017
collection = db.mynewcollection

def processMessage(msg):
    if not msg:
        return ""
    return msg.split()[0]

def retrieveAslUrl(word):
    dbObject = collection.find_one({'word': word})
    print(dbObject)
    if dbObject != None:
        return dbObject['link']
    return None


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        phone = request.form.get("phone", 0, type=int)
        message = request.form.get("message", "", type=str)
        print(request.form)
        processedMessage = processMessage(message)
        aslUrl = retrieveAslUrl(processedMessage)
        if aslUrl == None or phone == 0 or message == "":
            return render_template("index.html",  variable = None)

        return render_template("index.html", variable = aslUrl)

    return render_template("index.html",  variable = None)

if __name__ == "__main__":
    manager.run()
