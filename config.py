# -*- coding: cp1251 -*-
import os

BASE_DIR = os.path.dirname(__file__).encode('cp1251')
 
CSRF_ENABLED = True

SECRET_KEY = 'qwq33223rqwfs35tg5ga@#$@#sdf0audf0uasd[f[fj2%@#$@#lpwefj'

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, r"app\db\app.db").encode('1251')
SQLALCHEMY_MIGRATE_REPO =  os.path.join(BASE_DIR, r"app\db\db_repo").encode('1251')


