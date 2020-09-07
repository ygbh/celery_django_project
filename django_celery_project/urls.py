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

urlpatterns = [
    path('async_add/', views.async_add_task),
    path('async_mul/', views.async_mul_task),
    path('async_xsum/', views.async_xsum_task),
    path('sync_add/', views.sync_add_task),
    path('sync_mul/', views.sync_mul_task),
    path('sync_xsum/', views.sync_xsum_task),
]
