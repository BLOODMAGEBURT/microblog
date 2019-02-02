# -*- coding: utf-8 -*-
from flask import Blueprint
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       burt
   date：          2019-02-02
-------------------------------------------------
   Change Activity:
                   2019-02-02:
-------------------------------------------------
"""

bp = Blueprint('auth', __name__)
from app.auth import routes
