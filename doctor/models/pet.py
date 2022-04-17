from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=256, verbose_name='宠物名')
    age = models.IntegerField(default=0, verbose_name='年龄')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, default='',verbose_name='所属用户')

    class Meta:
        verbose_name = '宠物信息'
        verbose_name_plural = '宠物信息'

    def __str__(self):
        return self.name
