# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
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
app.config.from_object(Config)
# init db
db = SQLAlchemy(app)
# init migrate
migrate = Migrate(app, db)
from app import routes, models