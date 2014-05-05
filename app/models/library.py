#-*- coding: cp1251 -*-
from app import app
from app import db
from flask import request
from sqlalchemy import or_
import datetime
import json


class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    second_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30), nullable=True)
    def __init__(self, name, second, last):
        self.name = name
        self.second_name = second
        self.last_name = last
    def __repr__(self):
        return (self.name +" "+ self.second_name).encode('cp1251')
    def get_json(self):
        self.fields = dict(name = self.name.encode('utf-8'), second_name = self.second_name.encode('utf-8'), last_name = self.last_name.encode('utf-8'))
        return dict(id = self.id, class_name = "Author", fields = self.fields)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60), unique = True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    add_date = db.Column(db.Date)
    def __init__(self, name, author):
        self.name = name.encode('cp1251')
        self.author_id = author
        self.add_date = datetime.datetime.now()
    def __repr__(self):
        return self.name.encode('cp1251')
    def get_json(self):
        self.fields = dict(name = self.name.encode('utf-8'), author = self.author_id)
        return dict(id = self.id, class_name = "Book", fields = self.fields)
    

