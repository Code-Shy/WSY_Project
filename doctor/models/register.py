from django.db import models
from doctor.models.customer import Customer


class Register(models.Model):
    doctor = models.CharField(max_length=256, verbose_name='主治医生')
    time = models.DateTimeField(max_length=19, verbose_name='挂号时间')
    price = models.FloatField(default=0.0, verbose_name='价钱')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='用户')

    class Meta:
        verbose_name = '挂号信息'
        verbose_name_plural = '挂号信息'

    def __str__(self):
        return str(self.id)