#-*- coding: utf-8 -*-

from app import app
from forms.login import *
from models.users import *
from flask import Response, request,  session, redirect


@app.route("/login/", methods = ["POST"])
def login():
    # Функция авторизации\аутентификации пользователей
    if request.method == "POST":
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(nickname = form.nickname.data).first()
            if user and user.password == form.password.data:
                user.is_online = True
                user.last_visite_date = datetime.datetime.now()
                db.session.commit()
                session['user'] = user.id
    return redirect('/')

@app.route("/logout/", methods = ["GET"])
def logout():
    # Функция авторизации\аутентификации пользователей
    if request.method == "GET":
        if "user" in session:
            user = User.query.filter_by(id = session['user'], is_online = True).first()
            user.is_online = False
            user.last_visite_date = datetime.datetime.now()
            db.session.commit()
            del session['user']
    return redirect('/')

@app.route('/registration/', methods = ["POST"])
def registration():
    # Функция регистрации
    if request.method == "POST":
        form = RegistrationForm()
        if form.validate_on_submit():
            if form.password.data == form.password2.data:
                try:
                    new_user = User(nickname = form.nickname.data, password = form.password.data)
                    db.session.add(new_user)
                    db.session.commit()
                    session['user'] = new_user.id
                except:
                    return redirect('/')
    return redirect('/')

def get_user(category_id = None):
    # Функция выбирает пользователя из базы данных, 
    # если он есть в сессии и имеет статус "онлайн"
    user = None
    if "user" in session:
        if category_id:
            user = User.query.filter_by(id=session['user'], is_online = True, category_id = category_id).first()
        else:     
            user = User.query.filter_by(id=session['user'], is_online = True).first()
    return user
