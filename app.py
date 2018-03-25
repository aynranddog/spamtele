from flask import Flask, render_template, request
import telegram
from logging import FileHandler, WARNING
from bots import Spam

#https://api.telegram.org/botapikey/setWebhook?url=https://spamtele.herokuapp.com/spam

app = Flask(__name__)

file_handler = FileHandler("error.text")
file_handler.setLevel(WARNING)

@app.route("/", methods=["POST", "GET"])
def setWebhook():
    if request.method == "GET":
        print ("Done")
        return render_template ("index.html")

app.logger.addHandler(file_handler)

@app.route("/spam", methods = ["POST"])
def gr():
    gr = Spam()
    bot = telegram.Bot(token = key)
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True),bot)
        if update is None:
            return ("Show me your TOKEN please!")
        elif update.message != None:
            gr.pmhandel(update.message)
        return ("ok")

@app.errorhandler(404)
def notfound(e):
    return ("Don't wonder around, kid! JK!")
