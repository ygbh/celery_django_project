from __future__ import absolute_import, unicode_literals

"""django_celery_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from app01 import views
from app_log import views as log_views

urlpatterns = [
    path('async_add/', views.async_add_task),  # 主演示指定exchange+queue+routing key,来任务调用,函数传普通参数
    path('sync_add/', views.sync_add_task),  # 主演示,直接任务调用,函数传普通参数
    path('sync_add/', views.sync_add_task),  # 主演示,直接任务调用,函数传普通参数
    path('async_xsum/', views.async_xsum_task),  # 主演示,直接任务调用,函数传列表参数
    path('sync_xsum/', views.sync_xsum_task),  # 主演示,直接任务调用,函数传列表参数
    path('app01/async_add/', views.async_route_add_task),  # app01,主要演示手动路由
    path('app01/sync_add/', views.sync_route_add_task),  # app01,主要演示自动路由
    path('app_log/async_log/', log_views.async_route_handler_log),  # app_log,主要演示手动路由
    path('app_log/sync_log/', log_views.sync_route_handler_log),  # app_log,主要演示自动路由
]
