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

# 默认的队列，这个只有标识作用
CELERY_TASK_DEFAULT_QUEUE = 'celery'

# 定义队列规则，主要是给apply_async函数，调用任务的时候使用
CELERY_TASK_QUEUES = {
    Queue("celery", Exchange("celery"), routing_key="celery.default"),  # 默认队列
    Queue("feed_tasks", Exchange(name="default", type='topic'), routing_key="task.#"),
    # 定义队列feed_tasks,从交换接口:default接收，并且过滤路由的key,主要演示手动路由的机制
    Queue("add_queue", Exchange("compute_node"), routing_key="add_task"),  # 定义队列:add_queue,绑定交换机:compute_node
    Queue("mul_queue", Exchange("compute_node"), routing_key="mul_task"),  # 定义队列:mul_queue,绑定交换机:compute_node
    Queue("xsum_queue", Exchange("compute_node"), routing_key="xsum_task")  # 定义队列:xsum_queue,绑定交换机:compute_node
}

# 定义自动路由规则，主要是给delay函数，调用任务的时候使用，【元组方式定义】，顺序匹配执行
# 参考官方文档：https://docs.celeryproject.org/en/stable/userguide/routing.html#exchange-types
# CELERY_TASK_ROUTES = ([
#                           ('app01.tasks.*', {"queue": "app01"}),
#                           ('app_log.tasks.*', {"queue": "app_log"}),
#                       ],)

# # 定义自动路由规则，主要是给delay函数，调用任务的时候使用，【字典方式定义】
# CELERY_TASK_ROUTES = {
#     'app01.tasks.*': {"queue": "app01"},
#     'app_log.tasks.*': {"queue": "app_log"}
# }

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
