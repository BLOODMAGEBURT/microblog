# -*- coding: utf-8 -*-
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
"""
-------------------------------------------------
   File Name：     views
   Description :
   Author :       burt
   date：          2018-11-25
-------------------------------------------------
   Change Activity:
                   2018-11-25:
-------------------------------------------------
"""


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login required for username = %s and remember me = %s' % (form.username.data, str(form.remember_me.data)))
        return redirect(url_for('index'))
    return render_template('login.html',
                           title='Sign In',
                           form=form)
