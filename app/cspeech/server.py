# server.py
from flask import Flask, render_template, flash, request, redirect
from flask_script import Manager
from pymongo import MongoClient
from twilio.rest import Client


app = Flask(__name__)
app.config['SECRET_KEY'] = "hard"
manager = Manager(app)

dbClient = MongoClient("mongodb://admin:admin1@ds227555.mlab.com:27555/sdhacks2017")
db = dbClient.sdhacks2017
collection = db.mynewcollection

# Your Account SID from twilio.com/console
account_sid = "AC5dc87d69ac0191b2ee1ebaf22027d288"
# Your Auth Token from twilio.com/console
auth_token  = "5a4e5ab9890082dc50cbc223f9b8dd2e"
twilioNumber = "+14243737186"
twilioClient = Client(account_sid, auth_token)


def processMessage(msg):
    if not msg:
        return ""
    return msg.split()[0].lower()

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

        message = twilioClient.messages.create(
            to="+1"+str(phone),
            from_=twilioNumber,
            body=processedMessage,
            media_url=[aslUrl])
        print(processedMessage + " with " + aslUrl + "sent to " + str(phone) + " MID: " + str(message.sid))
        return render_template("index.html", variable = aslUrl)

    return render_template("index.html",  variable = None)

if __name__ == "__main__":
    manager.run()
