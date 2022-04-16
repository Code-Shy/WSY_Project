from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='姓名')
    num = models.CharField(max_length=256, default='', verbose_name='编号')
    password = models.CharField(max_length=256, default='', verbose_name='密码')
    age = models.CharField(max_length=256, default=None, verbose_name='年龄')
    sector = models.CharField(max_length=256, verbose_name='科室')
    phone = models.CharField(max_length=256, default='', verbose_name='手机号')

    class Meta:
        verbose_name = "医生信息"
        verbose_name_plural = "医生信息"

    def __str__(self):
        return str(self.user)
