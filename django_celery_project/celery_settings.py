# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6
# @Author  : suk
# @File    : celery_settings.py
# @Software: PyCharm
from __future__ import absolute_import, unicode_literals
# Celery settings
from kombu import Queue, Exchange
from celery.schedules import crontab

# 中间件的地址，这里使用RabbitMQ
CELERY_BROKER_URL = 'pyamqp://development:root@192.168.2.129:5672//development_host'

# 处理结果存储，可使用redis\MQ\MySQL,这里使用RabbitMQ
CELERY_RESULT_BACKEND = 'rpc://development:root@192.168.2.129:5672//development_host'
# CELERY_RESULT_BACKEND = 'django-db' # 这个是django-celery-results,会创建表，保存我们执行的结果，生产不推荐，必须自己获取结果存储，比较灵活些

# 设置时区,必须设置，防止定时任务时间不准备
CELERY_TIMEZONE = 'Asia/Shanghai'

# UTC时区换算关闭
CELERY_ENABLE_UTC = False

# 任务序列化
CELERY_TASK_SERIALIZER = 'json'

# 结果序列化
CELERY_RESULT_SERIALIZER = 'json'

# 接收的数据类型
CELERY_ACCEPT_CONTENT = ['json']

# 设置默认的队列default
CELERY_TASK_DEFAULT_QUEU = "celery"

# 定义队列
CELERY_TASK_QUEUES = {
    Queue("celery", Exchange("celery"), routing_key="celery"),
    Queue("add_queue", Exchange("compute_node"), routing_key="add_task"),  # 定义队列:add_queue,绑定交换机:compute_node
    Queue("mul_queue", Exchange("compute_node"), routing_key="mul_task"),  # 定义队列:mul_queue,绑定交换机:compute_node
    Queue("xsum_queue", Exchange("compute_node"), routing_key="xsum_task")  # 定义队列:xsum_queue,绑定交换机:compute_node
}

# 配置定时周期的任务
# 参考官方文档：https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#available-fields
CELERY_BEAT_SCHEDULE = {
    # test_task1 ==> 'schedule': 3.0,定义几秒即可
    # 'test_task1': {
    #     'task': 'app01.tasks.start_cycle_task',
    #     'schedule': 3.0,
    #     'args': (16, [1, 2, 3])
    # },
    # test_task2 ==> ’crontab()’,设定时期时间，跟Linux的crontab，差不多
    'test_task2': {
        'task': 'app01.tasks.start_cycle_task',
        'schedule': crontab(month_of_year='9', day_of_month='9', minute='*/1'),  # 设置9月9日，每一分钟执行一次
        'args': (16, [1, 2, 3])
    },
}

# 定义路由
# CELERY_ROUTES = {
#     'tasks.add.taskA': {"queue": "for_add_task_A", "routing_key": "for_task_A"},
#     'tasks.mul.taskB': {"queue": "for_mul_task_B", "routing_key": "for_task_B"}
# }
