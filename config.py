# -*- coding: utf-8 -*-
import os
"""
-------------------------------------------------
   File Name：     config
   Description :
   Author :       burt
   date：          2018-11-26
-------------------------------------------------
   Change Activity:
                   2018-11-26:
-------------------------------------------------
"""


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-xu_bo_bo'
    OPENID_PROVIDERS = [
        {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
        {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
        {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
        {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
        {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

    basedir = os.path.abspath(os.path.dirname(__file__))

    print(basedir)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # config admin email
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.vocoor.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 0
    MAIL_USERNAME = os.environ.get('xujianbo@vocoor.com')
    MAIL_PASSWORD = os.environ.get('cptbtptp804826$')
    ADMINS = ['wanghuina@vocoor.com']
