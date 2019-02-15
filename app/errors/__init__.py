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

bp = Blueprint('errors', __name__)
from app.errors import handlers
