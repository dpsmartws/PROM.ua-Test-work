# -*- coding: cp1251 -*-
from flask.ext.wtf import Form
from flask.ext.wtf.html5 import  EmailField
from wtforms import TextField, BooleanField, PasswordField  
from wtforms.validators import Required


class LoginForm(Form):
    nickname = TextField(u"�������", default =  u"��� ��������")
    password = TextField(u"������", default = u"������")
    

class RegistrationForm(Form):
    nickname = TextField(u"�������",)
    password = TextField(u"������")
    password2 = TextField(u"������")
    