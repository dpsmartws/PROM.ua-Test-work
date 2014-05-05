#-*- coding: cp1251 -*-
from flask import request,  redirect, session, Response, render_template
from app import app
from models.library import *
from models.users import *
from users_views import get_user


@app.route("/library/search", methods = ['POST','AJAX'])
def search():
    # Поиск книг
    books = {}
    authors = {}
    if request.form.has_key('search_string'):
        if request.form['search_string']:
            search_string = request.form['search_string']
            #sql_string = r"SELECT * FROM Book WHERE LOWER(name) LIKE LOWER('%%%s%%')" % search_string   
            #books = db.engine.execute(sql_string)
            #sql_string = r"SELECT * FROM Author WHERE LOWER(name) or LOWER(second_name) or LOWER(last_name) LIKE LOWER('%%%s%%')" % (search_string) 
            #authors = db.engine.execute(sql_string)
            books = Book.query.filter(Book.name.ilike("%"+search_string+"%")).all()   # CASE Не реагирует на кириллицу - проверить в дальнейшем
            authors = Author.query.filter(or_(Author.name.ilike("%"+search_string+"%"), Author.second_name.ilike("%"+search_string+"%"), Author.last_name.ilike("%"+search_string+"%"))).all()   # CASE Не работает с кириллицей - проверить в дальнейшем
            serialized = json.dumps([obj.get_json() for obj in list(books)+list(authors)])
            return serialized

@app.route("/library/load", methods = ['POST','AJAX'])
def load():
    # Поиск книг
    user = get_user(category_id = 1)
    if user:
            objects = {}
            if request.form.has_key('load'):
                if request.form['load']:
                    load = request.form['load']
                    if load == "books":
                        objects = Book.query.all()
                    elif load == "authors":
                        objects = Author.query.all() 
                    if objects:
                        serialized = json.dumps([obj.get_json() for obj in objects])
                        return serialized
                    
                        



@app.route('/library/delete', methods=['AJAX','POST'])
def delete():
    # Поиск книг
    user = get_user(category_id = 1)
    if user and request.form.has_key('class_name') and request.form.has_key('id'):
            class_name = request.form['class_name']
            id = request.form['id']
            if class_name == "book":
                book = Book.query.get(id)
                db.session.delete(book)
                db.session.commit()
            if class_name == "author":
                author = Author.query.get(id)
                #books = Book.query.filter_by(author_id = author.id)   # Выборка книг, привязанных к автору
                #db.session.delete(books)     # Удаление книг, привязанных к автору
                db.session.delete(author)
                db.session.commit()
            return Response(True)
            
            
@app.route('/author/<int:id>', methods=['GET','POST','AJAX'])
def show_author(id):
    if request.method == "GET":
        user = get_user()
        if user:
            current_link = "/author"
            author = Author.query.get(id)
            books = Book.query.filter_by(author_id = author.id)
            return render_template('index.html', user = user, author=author, books=books, current_link=current_link)
    if request.method == "POST":
        user = get_user(1)         # Доступно только администратору
        if user and request.form.has_key('id') and request.form.has_key('class_name'):
            class_name = request.form['class_name']
            id = request.form['id']
            if not int(id):
                author = Author(name = '', second = '', last = '')
            else:
                author = Author.query.get(id)
            serialized = json.dumps(author.get_json()) 
            return serialized
        
@app.route('/book/<int:id>', methods=['GET','POST','AJAX'])
def show_book(id):
    if request.method == "GET":
        user = get_user() 
        if user:
            current_link = "/book"
            book = Book.query.get(id)
            author = Author.query.get(book.author_id)
            return render_template('index.html', user = user, author=author, book=book, current_link=current_link)
    if request.method == "POST":
        user = get_user(1)      # Доступно только администратору
        if user and request.form.has_key('id') and request.form.has_key('class_name'):
            class_name = request.form['class_name']
            id = request.form['id']
            if not int(id):
                book = Book(name = '', author = '')
            else:
                book = Book.query.get(id)
            serialized = json.dumps(book.get_json())
            return serialized
            
            
@app.route('/library/edit', methods=['GET','AJAX','POST'])
def edit():
    user = get_user(1)          # Доступно только администратору
    if user and request.form.has_key('id') and request.form.has_key('class_name'):
        class_name = request.form['class_name']
        id = request.form['id']
        if class_name == "book":
            name = request.form['name']
            author_id =  request.form['author_id']
            if id == "null":
                book = Book(name = name, author = author_id)
                db.session.add(book)
            else:
                book = Book.query.get(id)
                book.name = name
                book.author_id = author_id
            db.session.commit()
        if class_name == "author":
            name = request.form['name']
            second_name = request.form['second_name']
            last_name = request.form['last_name']
            if id == "null":
                author = Author(name = name, second = second_name, last = last_name)
                db.session.add(author)
            else:
                author = Author.query.get(id)
                author.name = name
                author.second_name = second_name
                author.last_name = last_name
            db.session.commit()
        return redirect('/')
            
            
