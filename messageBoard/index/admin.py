from django.contrib import admin
from .models import *

# Register your models here.
admin.sites.site_title = '信息反馈后台系统'  # 修改title
admin.sites.site_header = '信息反馈平台'  # 修改header


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """注册Message
    """
    list_display = ['id', 'name', 'content', 'timestamp']  # 设置数据列表页显示的字段
    search_fields = ['name']  # 设置数据列表页的搜索框允许搜索的字段
    list_filter = ['name']  # 设置数据列表页右侧过滤器筛选和查找的字段
    ordering = ['id']  # 排序
    date_hierarchy = 'timestamp'  # 设置数据列表页日期选择器，只能设置日期字段

