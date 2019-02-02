# -*- coding: utf-8 -*-
from flask import render_template
from app import db
from app.errors import bp
"""
-------------------------------------------------
   File Name：     handlers
   Description :
   Author :       burt
   date：          2019-02-02
-------------------------------------------------
   Change Activity:
                   2019-02-02:
-------------------------------------------------
"""


@bp.app_errorhandler(404)
def file_not_found(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
