# -*- coding: utf-8 -*-
"""定义表单类
时间: 2020/9/7 16:10

作者: nola

更改记录:

重要说明:
    在模板文件index.html中使用表单实现信息提交功能
"""
from django import forms
from .models import *


class MessageModelForm(forms.ModelForm):
    """信息反馈表单类
    """
    class Meta:
        """信息反馈表单Meta类
        """
        model = Message
        fields = '__all__'

