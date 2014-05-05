#-*- coding: utf-8 -*-
import os
import datetime
from app import app
from flask import render_template, request, session, redirect
from forms.login import *
from models.users import *
from models.library import *
from users_views import *
from library_views import *



@app.route("/")
def main():
    # �������� �������
    current_link = "/"
    loginform = LoginForm()
    registrationform = RegistrationForm()
    user = get_user()
    return render_template("index.html", current_link=current_link, loginform=loginform, registrationform=registrationform, user = user)



@app.route('/static/<path:filename>')
def get_static(filename):
    # ������� �������� �������
    return app.send_static_file(os.path.join('static', filename))
    
    

@app.route("/<option>/")
def other(option):
    # ������� �������������� �������, �� ��������� � ����������� ���������
    # � ����� ������ - ������ ������� �������� � ��������� �����������
    current_link = "/"+option
    user = get_user()
    return render_template("index.html", current_link=current_link, user = user)    
    
      

        