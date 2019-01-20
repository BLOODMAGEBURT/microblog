# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import views, models
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       burt
   date：          2018-11-25
-------------------------------------------------
   Change Activity:
                   2018-11-25:
-------------------------------------------------
"""

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
# from app import views, models