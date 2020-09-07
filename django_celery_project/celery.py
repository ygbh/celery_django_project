# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6
# @Author  : suk
# @File    : celery.py
# @Software: PyCharm
# 绝对导入，解决 celery.py模块就不会与库冲突
from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# 设置Django项目的配置文件
from django_celery_project import celery_settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')

# 配置celery配置文件的位置
# 官网设置方法，直接集成在settings.py里面，并且前缀以CELERY_*,开头进行设置，不推荐,使settings.py变得更复杂
# app.config_from_object('django.conf:settings', namespace='CELERY')

# 使用新建一个celery_settings.py，专门配置celery所需要的参数
app.config_from_object(celery_settings, namespace='CELERY')

# 自动发现项目所有app中包含文件名为tasks.py，加载所有任务到内存中
app.autodiscover_tasks()


@app.task(bind=True)  # bind=True,可以调用本身self类的对象
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
