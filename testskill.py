# -*- coding: utf-8 -*-

from flask import Flask
from flask_ask import Ask, statement, question, session
import locale

locale.setlocale(locale.LC_ALL,'de_DE')

app = Flask(__name__)
ask = Ask(app, "/testskill")

@ask.launch
def start_skill():
    msg1 = "Das ist eine Meldung die Alexa beim Start ausgibt"
    return statement(msg1)

@ask.intent("info")
def infoIntent():
    msg1 = "Dieses Skill zeigt nur den allgemeinen Aufbau eines Alexa Skills mit Python und Flask Ask"
    return statement(msg1)

@ask.intent('AMAZON.HelpIntent')
def help():
    msg1 = "Hilfe text"
    return statement(msg1)

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
app.run(debug=True)
