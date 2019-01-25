# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler
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

app = Flask(__name__)  # type:Flask
app.config.from_object(Config)
# init db
db = SQLAlchemy(app)  # type:SQLAlchemy
# init migrate
migrate = Migrate(app, db)
# flask-login
login = LoginManager(app)
login.login_view = 'login'

# send error email
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'],
            subject='Microblog Failure',
            credentials=auth,
            secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
from app import routes, models, errors