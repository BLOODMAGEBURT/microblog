# -*- coding: utf-8 -*-
import os
from app import creat_app
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
    app = creat_app()
    # 解决 debug 模式下 启动两次的问题
    # 详见：https://www.kancloud.cn/hx78/python/450124
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        print('well done, good job ')
        print('password has been set')
    app.run(debug=False)



