import requests
from flask import Flask, render_template, url_for
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/time")
def present_time():
    return render_template("time.html")


@app.route("/quote")
def quotes():
    r = requests.get("https://api.kanye.rest")
    ust = r.text
    return render_template("quote.html", ust=ust)


if __name__ == "__main__":
    app.run(debug=True)
