# -*- coding: utf-8 -*-
"""定义信息反馈页面路由
时间: 2020/9/7 16:12

作者: nola

更改记录:

重要说明:
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
]
