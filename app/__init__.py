# -*- coding: utf-8 -*-
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel
import ssl
from elasticsearch import Elasticsearch
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

# init db
db = SQLAlchemy()
# init migrate
migrate = Migrate()
# flask-login
login = LoginManager()
login.login_view = 'auth.login'
# email
mail = Mail()

# bootstrap
bootstrap = Bootstrap()

# moment
moment = Moment()

# babel
babel = Babel()
# 忽略ssl验证
ssl._create_default_https_context = ssl._create_unverified_context


def create_app(config_class=Config):
    app = Flask(__name__)  # type:Flask
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    babel.init_app(app)

    app.elasticsearch = Elasticsearch(app.config.get('ELASTICSEARCH_URL')) if app.config['ELASTICSEARCH_URL'] else None

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # send error email
    if not (app.debug or app.testing):
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr=app.config['MAIL_USERNAME'],
                toaddrs=app.config['ADMINS'],
                subject='Microblog Failure',
                credentials=auth,
                secure=secure
            )
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

        # log into the file
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler(
            filename=app.config['LOG_FILE'],
            maxBytes=10240,
            backupCount=10
        )
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: '
                                                    '%(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Microblog startup')

    return app


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])


from app import models
from app.main import routes
