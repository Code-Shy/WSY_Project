from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='姓名')
    age = models.CharField(max_length=256, verbose_name='年龄')
    sector = models.CharField(max_length=256, verbose_name='科室')

    class Meta:
        verbose_name = "医生"
        verbose_name_plural = "医生"

    def __str__(self):
        return str(self.user)
