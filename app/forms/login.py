# -*- coding: cp1251 -*-
from flask.ext.wtf import Form
from flask.ext.wtf.html5 import  EmailField
from wtforms import TextField, BooleanField, PasswordField  
from wtforms.validators import Required


class LoginForm(Form):
    nickname = TextField(u"Никнейм", default =  u"Имя аккаунта")
    password = TextField(u"Пароль", default = u"Пароль")
    

class RegistrationForm(Form):
    nickname = TextField(u"Никнейм",)
    password = TextField(u"Пароль")
    password2 = TextField(u"Повтор")
    
