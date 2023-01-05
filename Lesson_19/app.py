from datetime import datetime
import requests
from flask import (Flask, abort, flash, redirect, render_template, request,
                   session, url_for)
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from valid import validator
import time

app = Flask(__name__)
moment = Moment(app)
app.config["SECRET_KEY"] = "7JU65T987YG564RDFjgyt7866uyt876fd4e6fy676yufy7"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)


# создание БД через основной скрипт
class Users(db.Model):
    '''описание таблицы для хранения учетных данных'''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    psw = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Users> {self.id}"


@app.route("/")
def index():
    '''главная страница'''
    return render_template("index.html")


@app.route("/time")
def present_time():
    '''страница время'''
    return render_template("time.html")


@app.route("/quote", methods=["POST", "GET"])
def quotes():
    '''страница цитат'''
    ust = []
    num = 1
    if request.method == "GET":
        for i in range(2):
            r1 = requests.get("https://api.kanye.rest")
            ust1 = r1.text
            ust1 = ust1[9:-1]
            ust.append(ust1)
        return render_template("quote.html", ust=ust)


@app.route("/contakt", methods=["POST", "GET"])
def contakt():
    '''страница обратной связи'''
    if request.method == "POST":
        print(request.form)
        if len(request.form["username"]) > 2:
            flash("Сообщение отправлено", category="succes")
        else:
            flash("Ошибка отправки", category="error")
    return render_template("contakt.html")


@app.route("/regestr", methods=["POST", "GET"])
def reges():
    '''страница регистрации'''
    if request.method == "POST":
        print(request.form)
        a = request.form["username"]
        b = request.form["password"]
        c = request.form["email"]
        if validator.validate(a, b, c):  # валидация
            try:
                user = Users(title=a, psw=b, email=c)
                db.session.add(user)
                db.session.commit()
                time.sleep(3)
                flash("Регистрация прошла успешно",
                      category="success")
                return render_template("login.html")
            except Exception as t:
                print(t)
                flash("Ошибка добавления учетных данных", category="error")
        else:
            flash("Ошибка регистрации", category="error")
    else:
        return render_template("regestr.html")
    return render_template("regestr.html")


@app.route("/profile/<username>")
def profile(username):
    if "userLogged" not in session or session["userLogged"] != username:
        abort(401)
    return render_template("profile.html", username=username)


@app.route("/login", methods=["POST", "GET"])
def login():
    '''страница авторизации'''
    user = Users.query.all()
    log = []
    pas = []
    for i in user:
        log.append(i.title)
        pas.append(i.psw)

    buf_name = False  # флаг доступа
    if request.method == "POST":
        for i in range(len(log)):  # авторизация
            if (
                request.form["username"] == log[i]
                and request.form["password"] == pas[i]
            ):
                buf_name = True

    if "userLogged" in session:  # повторный вход
        return redirect(url_for("profile", username=session["userLogged"]))
    elif buf_name:
        session["userLogged"] = request.form["username"]
        return redirect(url_for("profile", username=session["userLogged"]))
    return render_template("login.html")


app.secret_key = "46s8df79sf7sd54v6d8f7gfgb4x6c5vb746f"


@app.route("/delsession")
def delsession():
    '''выход из аккаунта'''
    print(session["userLogged"])
    session.clear()
    session.modified = True
    return redirect(url_for("index"))


@app.route("/profile/<username>/read_post")
def read_post(username):
    '''страница чтения записей'''
    return render_template("read_post.html", username=username)


@app.route("/profile/<username>/write_post")
def write_post(username):
    '''страница добавления записей'''
    return render_template("read_post.html", username=username)


@app.errorhandler(404)
def page404(error):
    '''страница 404'''
    return render_template("page404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)


# autopep8 --in-place --aggressive --aggressive
