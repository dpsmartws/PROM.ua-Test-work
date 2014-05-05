#-*- coding: cp1251 -*-
from app import app
from app import db
import datetime


class Usercategory(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), unique = True)
    short_description = db.Column(db.String(150), nullable=True)
    def __repr__(self):
        return self.name.encode('cp1251')
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(26), unique = True)
    password = db.Column(db.String(16))
    category_id = db.Column(db.Integer, db.ForeignKey('usercategory.id'))
    is_online = db.Column(db.Boolean, default = False)
    last_visite_date = db.Column(db.Date)
    registration_date = db.Column(db.Date)
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password
        self.category_id = 2
        self.is_online = True
        self.last_visite_date = datetime.datetime.now()
        self.registration_date = datetime.datetime.now()
    def __repr__(self):
        return  self.nickname.encode('cp1251')
    
        
    
    