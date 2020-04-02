import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    Birthday = now.month == 4 and now.day ==2

    return render_template("birthday.html", Birthday = Birthday)
