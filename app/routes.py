# -*- coding: utf-8 -*-
from app import app, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm
from app.models import User

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
@login_required
def index():
    posts = [  # fake array of posts
        {
            'author': {'username': 'zoy'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'burt'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 是否已登录
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    if form.validate_on_submit():
        # 是否存在
        print('用户名：{}, 密码：{}'.format(form.username.data, form.password.data))
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        # 判断登陆后跳转地址
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=False)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))

    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>', methods=['GET'])
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', title='User', user=user, posts=posts)
