#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6
# @Author  : suk
# @File    : tasks.py
# @Software: PyCharm
from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task


@shared_task
def add(x, y):
    """
        求和函数
    :param x: int
    :param y: int
    :return: Number int
    """
    return x + y


@shared_task
def mul(x, y):
    """
        相乘函数
    :param x: int
    :param y: int
    :return: Number int
    """
    return x * y


@shared_task
def xsum(numbers):
    """
        列表求和函数
    :param numbers: list
    :return: Number int
    """
    return sum(numbers)


@shared_task(ignore_result=True)  # 生产为：ignore_result=False,自动调度任务，需要配置返回结果关闭，结果没有什么义意，不然数据会越来越多，导致中间件挂掉
def start_cycle_task(arg1, argv):
    """
        这个是测试定时任务的函数
    :param arg1: 传入参数
    :param argv: 传入列表
    :return: 返回'ok'
    """
    print('时间戳:' + str(int(time.time())))
    return 'ok'
