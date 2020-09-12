#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11
# @Author  : suk
# @File    : tasks.py
# @Software: PyCharm
from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def handler_log(log_content):
    """
        这里主要是处理写日志的函数，主要用于演示路由分发
    :param log_content:日志内容
    :return:
    """
    print('handler write log')
    return 'write log ok'
