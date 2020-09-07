#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6
# @Author  : suk
# @File    : tasks.py
# @Software: PyCharm
from __future__ import absolute_import, unicode_literals

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
