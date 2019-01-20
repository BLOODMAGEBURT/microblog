# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
"""
-------------------------------------------------
   File Name：     form
   Description :
   Author :       burt
   date：          2018-11-26
-------------------------------------------------
   Change Activity:
                   2018-11-26:
-------------------------------------------------
"""


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
