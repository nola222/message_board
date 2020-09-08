import os

from django.apps import AppConfig


# 修改App在Admin后台显示的名称
default_app_config = 'index.IndexConfig'


def get_current_app_name(_file):
    """获取当前app的名称

    Args:
        _file(str):

    Returns:
        app_name(str): App的名称

    """
    return os.path.split(os.path.dirname(_file))[-1]


class IndexConfig(AppConfig):
    """重写IndexConfig
    """
    name = get_current_app_name(__file__)
    verbose_name = '信息管理'
