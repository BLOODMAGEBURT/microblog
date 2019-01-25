# -*- coding: utf-8 -*-
import os
from app import app, db
from app.models import User, Post
"""
-------------------------------------------------
   File Name：     run
   Description :
   Author :       burt
   date：          2018-11-25
-------------------------------------------------
   Change Activity:s
                   2018-11-25:
-------------------------------------------------
"""

if __name__ == '__main__':
    # user = User(username='uda', email='uda@163.com')
    # db.session.add(user)
    # db.session.commit()

    # 解决 debug 模式下 启动两次的问题
    # 详见：https://www.kancloud.cn/hx78/python/450124
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        print('well done, good job ')
        # dy = User(username='dy', email='dy@163.com')  # type: User
        # dy.set_password('123456aa')
        # print(dy.password_hash)
        # db.session.add(dy)
        # db.session.commit()
        # burt = User.query.filter_by(username='burt').first()
        # burt.about_me = 'i am a coder, i am good at coding'
        # db.session.commit()
        print('password has been set')
    app.run(debug=True)
