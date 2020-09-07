# -*- coding: utf-8 -*-
"""定义jinjia2模板引起对象
时间: 2020/9/7 16:05

作者: nola

更改记录:

重要说明:
    用于解析外层模板
"""
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def environment(**options):
    """将jinja2模板定义到django环境中

    Args:
        **options(dict):  其他参数

    Returns:
        env(object): Environment

    """
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse
    })

    return env
