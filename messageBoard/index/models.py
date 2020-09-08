from django.db import models

# Create your models here.


class Message(models.Model):
    """信息反馈页面模型
    """
    id = models.AutoField('序号', primary_key=True, help_text='序号')
    name = models.CharField('名称', max_length=50, help_text='名称')
    content = models.CharField('信息内容', max_length=200, help_text='信息内容')
    timestamp = models.DateField('反馈时间', auto_now=True, help_text='反馈时间')

    def __str__(self):
        """admin后台显示的字段名称
        """
        return self.name

    class Meta:
        """信息反馈表Meta类设置模型Message在后台系统的名称
        """
        verbose_name = '信息反馈表'
        verbose_name_plural = verbose_name



