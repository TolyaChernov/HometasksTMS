import requests
from flask import Flask, make_response, render_template, request
from flask_moment import Moment

from valid import validator

app = Flask(__name__)
moment = Moment(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/time")
def present_time():
    return render_template("time.html")


@app.route("/quote", methods=["POST", "GET"])
def quotes():
    """страница цитат"""
    ust = []
    if request.method == "GET":
        num = request.args.get("number", default=1)
        num = int(num)
        for i in range(num):
            r1 = requests.get("https://api.kanye.rest")
            ust1 = r1.text
            ust1 = ust1[9:-1]
            ust.append(ust1)
        return render_template("quote.html", ust=ust)


@app.route("/register", methods=["GET", "POST"])
def register():
    """страница регистрации"""
    if request.method == "POST":
        login = request.form.get("login")
        email = request.form.get("email")
        password = request.form.get("password")
        if validator.validate(login, email, password):  # валидация
            result = make_response("valid", 202)
        else:
            result = make_response("no valid", 406)
        return result


if __name__ == "__main__":
    app.run(debug=True)
