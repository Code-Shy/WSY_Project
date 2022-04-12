from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=256, verbose_name='用户名')
    password = models.CharField(default=None, max_length=256, verbose_name='密码')
    name = models.CharField(max_length=256, verbose_name='姓名')
    email = models.CharField(max_length=256, verbose_name='邮箱')
    phone = models.CharField(max_length=256, verbose_name='手机号')

    class Meta:
        verbose_name = '客户'
        verbose_name_plural = '客户'

    def __str__(self):
        return self.username
